#!/usr/bin/env python3
from configuration import *
import logging
from logging.handlers import RotatingFileHandler
import datetime
import sys

# writing debugging files and specific points
def log(filename,xml):
    if DEBUGGING:
        open(filename, 'w').write(xml)

# writing which origin/destination was asked from NOVA
def log_entry(origin, destination, starttime,stoptime):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOGFILE, maxBytes=80000, backupCount=10)
    logger.addHandler(handler)
    tz = datetime.timezone.utc
    ft = "%Y-%m-%dT%H:%M:%S%z"
    t = datetime.datetime.now(tz=tz).strftime(ft)
    logstr='"'+t+'";"'+origin+'";"'+destination+"';"+starttime+"';"+stoptime
    logger.info(logstr)

# sets up the logger
def setup_custom_logger():
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    handler = RotatingFileHandler(LOGFILE, maxBytes=80000, backupCount=10)
    handler.setFormatter(formatter)

    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)

    logger = logging.getLogger("OJP2NOVA")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)

    return logger

# makes sure the log path exists
import pathlib
pathlib.Path("generated").mkdir(parents=True, exist_ok=True)
logger = setup_custom_logger()

