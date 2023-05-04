#!/usr/bin/env python3
from configuration import *
import logging
from logging.handlers import RotatingFileHandler
import datetime

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