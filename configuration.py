# CONFIGURATION:

# For keys and connection to NOVA contact opendata@sbb.ch if necessary.
# However, those access keys only are provided under special circumstances.
NOVA_URL_TOKEN = ""
NOVA_CLIENT_ID = ''
NOVA_CLIENT_SECRET = ''
NOVA_URL_API = ""
NOVA_STAMMDATEN_FILE="generated/nova_stammdaten.gz"
NOVA_STAMMDATEN_FILE_UNZIPPED="generated/nova_stammdaten.xml"
NOVA_PARKPLATZ_FILE = "generated/nova_parkplatz.csv"
# OJP_Token can be obtained at: https://opentransportdata.swiss/dev-dashboard
OJP_URL_API = "https://api.opentransportdata.swiss/ojp2020"
OJP_TOKEN = ""
OJP_FARE_TOKEN=""

DIDOK_PERMALINK = "https://opentransportdata.swiss/de/dataset/service-points-full/permalink"
HTTPS = False
SSL_KEYFILE = ''
SSL_CERTFILE = ''
HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8000
HTTP_SLUG = "ojp2023"
DEBUGGING = True
LOGFILE = "logs/my_log.log"
READTRIPREQUESTFILE = True
VATRATE = 8.1  # Percent
USE_HTA = False # if in the tests half price should be used
READFILE = []
#READFILE.append("input/input_oev_shart_plus_long.xml")
#READFILE.append("input/input_walk_only.xml")
#READFILE.append("input/input_Zuerich_Chur.xml")
#READFILE.append("input/input_Bern_Chur_SOB_Zukunft.xml" ) #time must be reset before run. Check if discounts exist on www.sbb.ch
#READFILE.append("input/input_Bern_Zweisimmen_BLS_Zukunft.xml")  #time must be reset before run. Check if discounts exist on www.sbb.ch
#READFILE.append("input/input_Visp_SaaS_Fee_problem_1_preis.xml") #1. class price problematic
READFILE.append("input/input_strange_price.xml")
#READFILE.append("input/input_Zuerich_Bern.xml")
#READFILE.append("input/input_Basel_Sargans.xml")
#READFILE.append("input/input_Bern_Interlaken_Ost.xml")
#READFILE.append("input/input_Bern_Interlaken_Gymnasium.xml")
#READFILE.append("input/input_Bern_Guisanplatz_Interlaken_Gymnasium.xml")
#READFILE.append("input/input_local.xml")
#READFILE.append("input/input_oev_shart_plus_long.xml")
#READFILE.append("input/input_sharing_intercity.xml")
#READFILE.append(input/input_sharing_only.xml")
#READFILE.append("input/input_odv_alone.xml")
#READFILE.append("input/input_demand_responsive_saturday_after_1500.xml")
#READFILE.append("input/input_bus_postauto.xml")
#READFILE.append("input/input_in_the_past_not_handeled_well_in_Preisauskunft.xml")
#READFILE.append("input/input_problematic_case_vasile.xml")
#READFILE.append("input/input_Europaplatz.xml")
#READFILE.append("input/input_aller_retour.xml")
READFILE.append("input/input_Bodensee.xml")


# if there exists a local_configuration it is used.
try:
    from local_configuration import *
except:
    pass