# CONFIGURATION:

# For keys and connection to NOVA contact opendata@sbb.ch if necessary.
# However, those access keys only are provided under special circumstances.
NOVA_URL_TOKEN = ""
NOVA_CLIENT_ID = ''
NOVA_CLIENT_SECRET = ''
NOVA_URL_API = ""

# OJP_Token can be obtained at: https://opentransportdata.swiss/dev-dashboard
OJP_URL_API = "https://api.opentransportdata.swiss/ojp2020"
OJP_TOKEN = ""

HTTPS = False
SSL_KEYFILE = ''
SSL_CERTFILE = ''
HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8000
HTTP_SLUG = "ojp2023"
DEBUGGING = True
LOGFILE = "generated/my_log.log"
READTRIPREQUESTFILE = True
VATRATE = 7.7  # Percent   TODO will change 1.1.2024!
# READFILE = "input/input_oev_shart_plus_long.xml"
# READFILE = "input/input_walk_only.xml"
# READFILE = "input/input_Zuerich_Chur.xml"
READFILE = "input/input_local.xml"
# READFILE = "input/input_oev_shart_plus_long.xml"
# READFILE = "input/input_sharing_intercity.xml"
# READFILE = "input/input_sharing_only.xml"
# READFILE = "input/input_odv_alone.xml"
# READFILE = "input/input_demand_responsive_saturday_after_1500.xml"
# READFILE = "input/input_bus_postauto.xml"
# READFILE = "input/input_in_the_past_not_handeled_well_in_Preisauskunft.xml"
# if there exists a local_configuration it is used.
try:
    from local_configuration import *
except:
    pass