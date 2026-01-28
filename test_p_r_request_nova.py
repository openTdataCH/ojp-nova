#!/usr/bin/env python3

import json
import traceback

import requests
import urllib3
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import xml_logger
from configuration import *
from nova import *
from ojp import Ojp

logger = logging.getLogger(__name__)

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}


def parse_nova_request(body: str) -> VertriebsServicePortTypeSoapv14ErstelleAngeboteInput:
    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(config)
    return parser.from_string(body[body.find('<'):], VertriebsServicePortTypeSoapv14ErstelleAngeboteInput)

#def parse_nova_request1() -> VertriebsServicePortTypeSoapv14ErstelleAngeboteInput:
#   config = ParserConfig(
    #        base_url=None,
    #        process_xinclude=False,
    #        fail_on_unknown_properties=False,
    #        fail_on_unknown_attributes=False,
    #    )
    #    parser = XmlParser(config)
    #    return VertriebsServicePortTypeSoapv14ErstelleAngeboteInput(
    #        body=VertriebsServicePortTypeSoapv14ErstelleAngeboteInput.Body(
    #           erstelle_preis_auskunft=ErstellePreisAuskunft(
    #               preis_auskunft_request=VerbindungPreisAuskunftRequest(kunden_segmente_gruppieren=False,
    #                                                                 client_identifier=ClientIdentifier(
    #                                                                     leistungs_vermittler=11, kanal_code=41,
    #                                                                     verkaufs_stelle=16437, vertriebs_punkt=16437,
    #                                                                     verkaufs_geraete_id="236"),
    #                                                                 correlation_kontext=CorrelationKontext(
    #                                                                    correlation_id="87482634-560b-4da3-b6a1-155c37490fed",
    #                                                                     geschaefts_prozess_id="1781786f-57ba-4e9a-bc29-287e2aa97f9a"),
    #                                                                 angebots_filter=[TaxonomieFilter(
    #                                                                    produkt_taxonomie="Basistaxonomie",
    #                                                                    taxonomie_klasse_pfad=[TaxonomieKlassePfad(
    #                                                                      klassen_name="Einzelbillette")])],
    #                                                              reisender=[ReisendenInfoPreisAuskunft(alter=30,
    #                                                                                                    externe_reisenden_referenz_id="1234",
    #                                                                                                    reisenden_typ=ReisendenTypCode.PERSON,
    #                                                                                                    ermaessigungs_karte_code=["HTA"])],
    #                                                              verbindung=[]
#                                                              ))))
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
            access_token_response = requests.post(NOVA_TOKEN_URL, data=data, verify=False, allow_redirects=False,
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

    location = NOVA_BASE_URL + NOVA_VERTRIEBS_PATH
    client = Client.from_service(VertriebsServicePortTypeSoapv14ErstelleAngebote, location=location, encoding="utf-8")
    client.parser = parser

    return client

def test_get_nova_request():
    astr="""<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header/>
  <soapenv:Body>
    <ns21:erstelleAngebote xmlns:ns22="http://nova.voev.ch/services/internal/leistungnotification" xmlns:ns21="http://nova.voev.ch/services/v14/vertrieb" xmlns:nova-leistungnotiz="http://nova.voev.ch/services/v14/leistungnotiz" xmlns:ns19="http://nova.voev.ch/services/v14/vertrag" xmlns:ns18="http://nova.voev.ch/services/internal" xmlns:vs="http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten" xmlns:nova-protokoll="http://nova.voev.ch/services/v14/vertrieb/protokoll" xmlns:nova-erneuerungsinfo="http://nova.voev.ch/services/v14/vertrieb/erneuerungsinfo" xmlns:ns14="http://nova.voev.ch/services/v14/kuko" xmlns:offlinemanagement="http://nova.voev.ch/services/v14/vertrieb/offlinemanagement" xmlns:nova-monitoring="http://nova.voev.ch/services/internal/monitoring" xmlns:nova-preisauskunft="http://nova.voev.ch/services/v14/preisauskunft" xmlns:vb="http://nova.voev.ch/services/v14/vertriebsbase" xmlns:base="http://nova.voev.ch/services/v14/base" xmlns:ns8="http://nova.voev.ch/services/v14/fachlichervertrag" xmlns:inkasso="http://nova.voev.ch/services/v14/inkasso" xmlns:nova-vertragskonto="http://nova.voev.ch/services/v14/vertragskonto" xmlns:novasp-swisspass="http://nova.voev.ch/services/v14/swisspass" xmlns:novakuko="http://nova.voev.ch/services/v14/kundeninteraktion" xmlns:novagp="http://nova.voev.ch/services/v14/geschaeftspartner" xmlns="http://nova.voev.ch/services/v14/vertrieb" xmlns:novavt-vertrag="http://nova.voev.ch/services/v14/vertragbase">
      <ns21:angebotsRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns21:ProduktBasierterAngebotsRequest" ns21:gueltigAbDatum="2024-02-02" ns21:gueltigAbZeit="10:00:00.000" ns21:standort="6209" ns21:kundenSegmenteGruppieren="false" ns21:fachlogLevel="OFF">
        <ns21:clientIdentifier base:leistungsVermittler="11" base:kanalCode="41" base:verkaufsStelle="16437" base:vertriebsPunkt="16437" base:verkaufsGeraeteId="236"/>
        <ns21:correlationKontext>
          <base:correlationId>05d26536-579f-49cc-9cde-383234987477</base:correlationId>
          <base:geschaeftsProzessId>512e62f5-6609-4861-b611-9d6f72aedd22</base:geschaeftsProzessId>
        </ns21:correlationKontext>
        <ns21:reisender ns21:externeReisendenReferenzId="1">
          <ns21:ohneTkid>
            <ns21:reisendenTyp>PERSON</ns21:reisendenTyp>
            <ns21:alter>20</ns21:alter>
            <ns21:ermaessigungsKarteCode>KEINE_ERMAESSIGUNGSKARTE</ns21:ermaessigungsKarteCode>
          </ns21:ohneTkid>
        </ns21:reisender>
        <ns21:angebotsFilter xsi:type="vb:ProduktNummerFilter">
          <vb:produktNummer>80029</vb:produktNummer>
        </ns21:angebotsFilter>
      </ns21:angebotsRequest>
    </ns21:erstelleAngebote>
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
        xml_logger.log_serialized('nova_response.xml',nova_response)
        return nova_response

def check_configuration():
    if (len(NOVA_CLIENT_SECRET)==0):
        print("Secrets not set in the configuration")
        exit(1)

if __name__ == '__main__':
    #check configuration
    ojp_trip_request_xml=''
    check_configuration()
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2"}
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=serializer_config)
    try:
        areqbody='''
        <?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header/>
  <soapenv:Body>
    <ns21:erstelleAngebote xmlns:ns22="http://nova.voev.ch/services/internal/leistungnotification" xmlns:ns21="http://nova.voev.ch/services/v14/vertrieb" xmlns:nova-leistungnotiz="http://nova.voev.ch/services/v14/leistungnotiz" xmlns:ns19="http://nova.voev.ch/services/v14/vertrag" xmlns:ns18="http://nova.voev.ch/services/internal" xmlns:vs="http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten" xmlns:nova-protokoll="http://nova.voev.ch/services/v14/vertrieb/protokoll" xmlns:nova-erneuerungsinfo="http://nova.voev.ch/services/v14/vertrieb/erneuerungsinfo" xmlns:ns14="http://nova.voev.ch/services/v14/kuko" xmlns:offlinemanagement="http://nova.voev.ch/services/v14/vertrieb/offlinemanagement" xmlns:nova-monitoring="http://nova.voev.ch/services/internal/monitoring" xmlns:nova-preisauskunft="http://nova.voev.ch/services/v14/preisauskunft" xmlns:vb="http://nova.voev.ch/services/v14/vertriebsbase" xmlns:base="http://nova.voev.ch/services/v14/base" xmlns:ns8="http://nova.voev.ch/services/v14/fachlichervertrag" xmlns:inkasso="http://nova.voev.ch/services/v14/inkasso" xmlns:nova-vertragskonto="http://nova.voev.ch/services/v14/vertragskonto" xmlns:novasp-swisspass="http://nova.voev.ch/services/v14/swisspass" xmlns:novakuko="http://nova.voev.ch/services/v14/kundeninteraktion" xmlns:novagp="http://nova.voev.ch/services/v14/geschaeftspartner" xmlns="http://nova.voev.ch/services/v14/vertrieb" xmlns:novavt-vertrag="http://nova.voev.ch/services/v14/vertragbase">
      <ns21:angebotsRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns21:ProduktBasierterAngebotsRequest" ns21:gueltigAbDatum="2024-02-02" ns21:gueltigAbZeit="10:00:00.000" ns21:standort="6209" ns21:kundenSegmenteGruppieren="false" ns21:fachlogLevel="OFF">
        <ns21:clientIdentifier base:leistungsVermittler="11" base:kanalCode="41" base:verkaufsStelle="16437" base:vertriebsPunkt="16437" base:verkaufsGeraeteId="236"/>
        <ns21:correlationKontext>
          <base:correlationId>05d26536-579f-49cc-9cde-383234987477</base:correlationId>
          <base:geschaeftsProzessId>512e62f5-6609-4861-b611-9d6f72aedd22</base:geschaeftsProzessId>
        </ns21:correlationKontext>
        <ns21:reisender ns21:externeReisendenReferenzId="1">
          <ns21:ohneTkid>
            <ns21:reisendenTyp>PERSON</ns21:reisendenTyp>
            <ns21:alter>20</ns21:alter>
            <ns21:ermaessigungsKarteCode>KEINE_ERMAESSIGUNGSKARTE</ns21:ermaessigungsKarteCode>
          </ns21:ohneTkid>
        </ns21:reisender>
        <ns21:angebotsFilter xsi:type="vb:ProduktNummerFilter">
          <vb:produktNummer>80029</vb:produktNummer>
        </ns21:angebotsFilter>
      </ns21:angebotsRequest>
    </ns21:erstelleAngebote>
  </soapenv:Body>
</soapenv:Envelope>
        '''
        nova_request=parse_nova_request(areqbody)
        nova_request_xml = serializer.render(nova_request)
        xml_logger.log_object_as_xml('nova_p_r_request.xml', nova_request)
        nova_client = get_nova_client()
        nova_response = nova_client.send(nova_request, headers=headers)
        if nova_response:
            xml_logger.log_object_as_xml('nova_p_r_response.xml', nova_response)
    except Exception as e:
        # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
        xml_logger.log_serialized('error_file.xml', str(e))
        logger.exception(e)
        print (str(e))
        print(traceback.format_exc())
