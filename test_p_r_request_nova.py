#!/usr/bin/env python3

import json
import requests
import urllib3
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from configuration import *
from test_create_ojp_request import *
from map_nova_to_ojp import test_nova_to_ojp
from map_ojp_to_nova import test_ojp_fare_request_to_nova_request
from map_ojp_to_ojp import parse_ojp, map_ojp_trip_result_to_ojp_fare_request #, map_ojp_trip_result_to_ojp_refine_request
from nova import PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft
from ojp import Ojp
from logger import log
import traceback

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

def parse_nova_request(body: str) -> PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft:
    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(config)
    return parser.from_string(body, PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft)
class OAuth2Helper:
    # Credits: https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code

    def __init__(self, client_id, client_secret):
        urllib3.disable_warnings()
        self.client_id = client_id
        self.client_secret = client_secret
        self.current_token = None

    def get_token(self, new_token=False):
        if new_token or not self.current_token:
            data = {'grant_type': 'client_credentials', 'scope': 'api://e1710a9f-d3e8-4751-b662-42f242e79f20/.default'}
            access_token_response = requests.post(NOVA_URL_TOKEN, data=data, verify=False, allow_redirects=False,
                                                  auth=(self.client_id, self.client_secret))
            self.current_token = json.loads(access_token_response.text)
        return self.current_token['access_token']

def get_nova_client():
    # TODO: It might be more elegant to cache this client in some way, but we would need to handle the expiry of the token
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2" }

    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(config)

    client = Client.from_service(PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft, location=NOVA_URL_API, encoding="utf-8")
    client.parser = parser

    return client

def test_get_nova_request():
    astr="""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
	<soapenv:Body>
		<nova-preisauskunft:erstellePreisAuskunft xmlns:base="http://nova.voev.ch/services/v14/base" xmlns:vb="http://nova.voev.ch/services/v14/vertriebsbase" xmlns:nova-preisauskunft="http://nova.voev.ch/services/v14/preisauskunft" xmlns:ns21="http://nova.voev.ch/services/v14/vertrieb" xmlns="http://nova.voev.ch/services/v14/vertrieb">
			<nova-preisauskunft:PreisAuskunftRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" nova-preisauskunft:kundenSegmenteGruppieren="false" nova-preisauskunft:gueltigAbDatum="2023-12-10" nova-preisauskunft:gueltigAbZeit="09:00:00" nova-preisauskunft:parkplatz="155">
				<nova-preisauskunft:clientIdentifier base:leistungsVermittler="11" base:kanalCode="41" base:verkaufsStelle="16437" base:vertriebsPunkt="16437" base:verkaufsGeraeteId="236"/>
				<nova-preisauskunft:correlationKontext>
					<base:correlationId>87482634-560b-4da3-b6a1-155c37490fed</base:correlationId>
					<base:geschaeftsProzessId>1781786f-57ba-4e9a-bc29-287e2aa97f9a</base:geschaeftsProzessId>
				</nova-preisauskunft:correlationKontext>
				<nova-preisauskunft:angebotsFilter>
					<vb:produktTaxonomie>Basistaxonomie</vb:produktTaxonomie>
					<vb:taxonomieKlassePfad>
						<vb:klassenName>Einzelbillette</vb:klassenName>
					</vb:taxonomieKlassePfad>
				</nova-preisauskunft:angebotsFilter>
<nova-preisauskunft:reisender>
<nova-preisauskunft:ohneTkid>
<nova-preisauskunft:reisendenTyp>PERSON</nova-preisauskunft:reisendenTyp>
<nova-preisauskunft:geschlecht>WEIBLICH</nova-preisauskunft:geschlecht>
<nova-preisauskunft:geburtsTag>1990-01-01</nova-preisauskunft:geburtsTag>
<nova-preisauskunft:ermaessigungsKarteCode>KEINE_ERMAESSIGUNGSKARTE</nova-preisauskunft:ermaessigungsKarteCode>
</nova-preisauskunft:ohneTkid>
</nova-preisauskunft:reisender>
<nova-preisauskunft:angebotsFilter>
<vb:produktNummer>84001</vb:produktNummer>
</nova-preisauskunft:angebotsFilter>
</nova-preisauskunft:PreisAuskunftRequest>
		</nova-preisauskunft:erstellePreisAuskunft>
	</soapenv:Body>
</soapenv:Envelope>
    """
    return astr
def test_nova_request_reply(ojp: Ojp):
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2"}
    nova_request = ojp
    nova_client = get_nova_client()
    nova_response = nova_client.send(nova_request, headers=headers)
    if nova_response:
        serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
        serializer = XmlSerializer(serializer_config)
        nova_response_xml = serializer.render(nova_response)
        log('generated/nova_response.xml',nova_response_xml)
        return nova_response

def check_configuration():
    if (len(NOVA_CLIENT_SECRET)==0):
        print("Secrets not set in the configuration")
        exit(1)

if __name__ == '__main__':
    #check configuration
    ojp_trip_request_xml=''
    check_configuration()
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)
    try:
        ojp_fare_request_xml = test_get_nova_request()
        log('generated/ojp_fare_p_r_request.xml',ojp_fare_request_xml)
        nova_request=parse_nova_request(ojp_fare_request_xml)
        nova_response = test_nova_request_reply(nova_request)
        if nova_response:
            ojp_fare_result = test_nova_to_ojp(nova_response)
            ojp_fare_result_xml = serializer.render(ojp_fare_result, ns_map=ns_map)
            for fr1 in ojp_fare_result.fare_result:
                for fr in fr1.trip_fare_result:
                    print ("Legs: "+str(fr.from_trip_leg_id_ref)+"-"+str(fr.to_trip_leg_id_ref))
                    print (fr.fare_product)
                    print ("\n")
            log('generated/ojp_fare_p_r_result.xml', ojp_fare_result_xml)

    except Exception as e:
        # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
        log('generated/error_file.xml', str(e))
        print (str(e))
        print(traceback.format_exc())
