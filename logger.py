#!/usr/bin/env python3
from configuration import *

def log(filename,xml):
    if DEBUGGING:
        open(filename, 'w').write(xml)
