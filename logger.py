import logging
from config import logPath

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=logPath)

logger = logging.getLogger()