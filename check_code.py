import subprocess
import sys
from logger import logger

def run_command(command: list[str], description: str) -> dict:
    logger.info(f"\n🛠️  Running: {description}")
    try:
        result = subprocess.run(command, check=False)
        return {"code": 0, "message": result.stdout}
    except FileNotFoundError:
        message = f"❌ Command not found: {' '.join(command)}"
        logger.critical(message)
        return {"code": 1, "message": message}
    except Exception as e:
        message = f"❌ Error while running {description}: {e}"
        logger.critical(message)
        return 1

def main():
    exit_code = 0

    # Run Bandit for security issues
    bandit_cmd = ["bandit", "-r", ".", "--exclude", "venv,wvenv", "-f", "json", "-o", "reports/bandit_report.json"]
    result = run_command(bandit_cmd, "Bandit (security linter)")
    exit_code |= result.get("code", 0)

    # Run pip-audit for dependency vulnerabilities
    pip_audit_cmd = ["pip-audit"]
    result = run_command(pip_audit_cmd, "pip-audit (dependency vulnerability check)")
    exit_code |= result.get("code", 0)

    if exit_code == 0:
        logger.info("\n✅ All checks passed.")
    else:
        logger.error("\n⚠️  Some checks failed.")

    sys.exit(exit_code)

if __name__ == "__main__":
    main()
