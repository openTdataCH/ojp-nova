# CONFIGURATION:
from typing import List
import logging
from ojp import VatRateEnumeration
from os import getenv

_enabled_values = ['true', 'enabled']

# For keys and connection to NOVA contact opendata@sbb.ch if necessary.
# However, those access keys only are provided under special circumstances.
NOVA_URL_TOKEN = getenv("NOVA_TOKEN_URL")
NOVA_CLIENT_ID = getenv("NOVA_CLIENT_ID")
NOVA_CLIENT_SECRET = getenv("NOVA_CLIENT_SECRET")
NOVA_SCOPE = getenv("NOVA_SCOPE")
NOVA_URL_API = getenv("NOVA_BASE_URL")
NOVA_STAMMDATEN_FILE="generated/nova_stammdaten.gz"
NOVA_STAMMDATEN_FILE_UNZIPPED="generated/nova_stammdaten.xml"
NOVA_PARKPLATZ_FILE = "generated/nova_parkplatz.csv"

# OJP_Token can be obtained at: https://opentransportdata.swiss/dev-dashboard
OJP_URL_API = "https://api.opentransportdata.swiss/ojp2020"
OJP_TOKEN = getenv("OJP_TOKEN")

OJP_2_URL_API = "https://api.opentransportdata.swiss/ojp20"
OJP_2_TOKEN = getenv("OJP2_TOKEN")
OJP_FARE_TOKEN=""

LOG_FILE_HANDLER_ENABLED = getenv("LOG_FILE_HANDLER_ENABLED", "true").lower() in _enabled_values
LOG_DIR = getenv("LOG_DIR", "logs")
LOG_FILE = LOG_DIR + "/my_log.log"
LOG_LEVEL = getenv("LOG_LEVEL", logging.getLevelName(logging.INFO))
DEBUGGING = True

DIDOK_PERMALINK = "https://opentransportdata.swiss/de/dataset/service-points-full/permalink"
HTTPS = False
SSL_KEYFILE = ''
SSL_CERTFILE = ''
HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8000
HTTP_SLUG = "ojp2023"
READTRIPREQUESTFILE = True
VATRATE= 8.1  # Percent
USE_HTA = True # if in the tests half price should be used
READFILE: List[str]  = [] # contains the test files to read

# if there exists a test_configuration it is loaded.
try:
    from test_configuration import *
except:
    pass
# if there exists a local_configuration it is used.
try:
    from local_configuration import *
except:
    pass