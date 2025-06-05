import subprocess
import sys
from logger import logger

def run_command(command: list[str], description: str) -> int:
    logger.info(f"\n🛠️  Running: {description}")
    try:
        result = subprocess.run(command, check=False)
        return result.returncode
    except FileNotFoundError:
        logger.critical(f"❌ Command not found: {' '.join(command)}")
        return 1
    except Exception as e:
        logger.critical(f"❌ Error while running {description}: {e}")
        return 1

def main():
    exit_code = 0

    # Run Bandit for security issues
    bandit_cmd = ["bandit", "-r", "."]
    exit_code |= run_command(bandit_cmd, "Bandit (security linter)")

    # Run pip-audit for dependency vulnerabilities
    pip_audit_cmd = ["pip-audit"]
    exit_code |= run_command(pip_audit_cmd, "pip-audit (dependency vulnerability check)")

    if exit_code == 0:
        logger.info("\n✅ All checks passed.")
    else:
        logger.error("\n⚠️  Some checks failed.")

    sys.exit(exit_code)

if __name__ == "__main__":
    main()
