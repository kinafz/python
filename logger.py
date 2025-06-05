import logging
from logging.handlers import RotatingFileHandler
from config import logPath

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(logPath, maxBytes=2000, backupCount=10),
        logging.StreamHandler()
    ])

logger = logging.getLogger()