import logging
import pathlib
import sys
import time
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from configuration import (
    LIVENESS_PATH,
    LOG_DIR,
    LOG_FILE,
    LOG_FILE_HANDLER_ENABLED,
    LOG_LEVEL,
    READINESS_PATH,
)

LOG_FORMAT = '%(asctime)s %(levelname)-8s - %(name)s: %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_FILE_MAX_BYTES = 8000000
LOG_FILE_BACKUP_COUNT = 10

class HealthCheckAccessFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        return LIVENESS_PATH not in message and READINESS_PATH not in message

class CustomFormatter(logging.Formatter):
    converter = time.localtime

    def format(self, record: logging.LogRecord) -> str:
        timestamp = self.formatTime(
            record,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        # Add milliseconds to the timestamp.
        timestamp = f"{timestamp}.{int(record.msecs):03d}"

        thread_name = record.threadName
        level = record.levelname
        logger_name = record.name

        message = record.getMessage()
        if record.exc_info:
            message += "\n" + self.formatException(record.exc_info)

        return (
            f"{timestamp} [{thread_name}] {level} "
            f"{logger_name} : {message}"
        )

def setup_logging() -> None:
    '''Initializes the logging configuration for this application.'''

    # formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
    console_handler = StreamHandler(stream=sys.stdout)
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(CustomFormatter())
    log_handlers = {console_handler}
    if LOG_FILE_HANDLER_ENABLED:
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_FILE_MAX_BYTES, backupCount=LOG_FILE_BACKUP_COUNT)
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(CustomFormatter())
        log_handlers.add(file_handler)
        pathlib.Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        level=LOG_LEVEL,
        handlers=log_handlers)

    # prevent request logs on health endpoints
    logging.getLogger("uvicorn.access").addFilter(HealthCheckAccessFilter())
