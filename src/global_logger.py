import logging
from logging.handlers import RotatingFileHandler

# Initialize the logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# Formatter for log messages
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Console handler (logs to the console)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File handler (logs to a file with rotation)
file_handler = RotatingFileHandler(
    "app.log", maxBytes=1024 * 1024, backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
