import logging
import pathlib
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from configuration import LOG_DIR, LOG_FILE, LOG_FILE_HANDLER_ENABLED, LOG_LEVEL

LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_FILE_MAX_BYTES = 8000000
LOG_FILE_BACKUP_COUNT = 10


def setup_logging():
    ''' Initializes the logging configuration for this application.'''

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
    console_handler = StreamHandler(stream=sys.stdout)
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)
    log_handlers = {console_handler}

    if LOG_FILE_HANDLER_ENABLED:
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT)
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(formatter)
        log_handlers.add(file_handler)
        pathlib.Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        level=LOG_LEVEL,
        handlers=log_handlers)
