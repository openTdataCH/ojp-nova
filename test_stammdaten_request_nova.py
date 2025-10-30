#!/usr/bin/env python3
import json
import requests
import urllib3
import gzip
import shutil
import csv
import xml.etree.ElementTree as ET
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from configuration import *
from map_nova_to_ojp import test_nova_to_ojp
from nova import *
from ojp import Ojp
from logger import log
from nova.get_stammdaten_file import *
from nova.vertriebsstammdaten_service_port_type_soapv14_get_stammdaten_file import *
from nova.vertriebsstammdaten_service_port_type_soapv14_get_stammdaten_file_output import *
from nova.vertriebsstammdaten_service_port_type_soapv14_get_stammdaten_file_input import  *
import traceback
from zipfile import ZipFile



ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

def load_didok_stammdaten():
    r0 = requests.get(DIDOK_PERMALINK)
    res = {}
    print (r0.url)
    r1 = requests.get(r0.url)  # using redirect
    chunk_size=200000
    with open(generated("servicepoints.zip"), "wb") as out:
        data =r1.content
        out.write(data)
    with ZipFile(generated("servicepoints.zip")) as myzip:
        myzip.extract(myzip.filelist[0],GENERATED_DIR)
        print(myzip.filelist[0].filename)
        # open the file and build
        with open(generated(myzip.filelist[0].filename), encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                lin=[]
                sloid= row[2]
                lin.append(sloid)
                didok=""
                try:
                    didok = str(100000*int(row[1])+int(row[0]))
                except:
                    #do nothing
                    print ("no valid didok")
                lin.append(didok)
                name= row[7]
                lin.append(name)
                lon= row[49]
                lin.append(lon)
                lat= row[50]
                lin.append(lat)
                res[name]=lin
    print(res["Bern"])
    return res
def parse_nova_stammdaten_request(body: str) -> VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileInput:
    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(config)
    return parser.from_string(body[body.find('<'):], VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileInput)

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

    client = Client.from_service(VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFile, location=NOVA_URL_S_API, encoding="utf-8")
    client.parser = parser

    return client

def test_get_nova_stammdaten_request():
    astr="""
<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header/>
  <soapenv:Body>
    <vs:getStammdatenFile xmlns:ns22="http://nova.voev.ch/services/internal/leistungnotification" xmlns:ns21="http://nova.voev.ch/services/v14/vertrieb" xmlns:nova-leistungnotiz="http://nova.voev.ch/services/v14/leistungnotiz" xmlns:ns19="http://nova.voev.ch/services/v14/vertrag" xmlns:ns18="http://nova.voev.ch/services/internal" xmlns:vs="http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten" xmlns:nova-protokoll="http://nova.voev.ch/services/v14/vertrieb/protokoll" xmlns:nova-erneuerungsinfo="http://nova.voev.ch/services/v14/vertrieb/erneuerungsinfo" xmlns:ns14="http://nova.voev.ch/services/v14/kuko" xmlns:offlinemanagement="http://nova.voev.ch/services/v14/vertrieb/offlinemanagement" xmlns:nova-monitoring="http://nova.voev.ch/services/internal/monitoring" xmlns:nova-preisauskunft="http://nova.voev.ch/services/v14/preisauskunft" xmlns:vb="http://nova.voev.ch/services/v14/vertriebsbase" xmlns:base="http://nova.voev.ch/services/v14/base" xmlns:ns8="http://nova.voev.ch/services/v14/fachlichervertrag" xmlns:inkasso="http://nova.voev.ch/services/v14/inkasso" xmlns:nova-vertragskonto="http://nova.voev.ch/services/v14/vertragskonto" xmlns:novasp-swisspass="http://nova.voev.ch/services/v14/swisspass" xmlns:novakuko="http://nova.voev.ch/services/v14/kundeninteraktion" xmlns:novagp="http://nova.voev.ch/services/v14/geschaeftspartner" xmlns="http://nova.voev.ch/services/v14/vertrieb" xmlns:novavt-vertrag="http://nova.voev.ch/services/v14/vertragbase">
      <vs:stammdatenFileRequest vs:leistungsVermittler="11" vs:kanalCode="41">
        <vs:correlationKontext>
          <base:correlationId>4fc5e857-33e4-4f0e-be31-a535349003d5</base:correlationId>
          <base:geschaeftsProzessId>512e62f5-6609-4861-b611-9d6f72aedd22</base:geschaeftsProzessId>
        </vs:correlationKontext>
      </vs:stammdatenFileRequest>
    </vs:getStammdatenFile>
  </soapenv:Body>
</soapenv:Envelope>
    """
    return astr
def test_nova_stammdaten_request_reply(ojp: Ojp):
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
        log('nova_stammdaten.xml',nova_response_xml)
        return nova_response

def check_configuration():
    if (len(NOVA_CLIENT_SECRET)==0):
        print("Secrets not set in the configuration")
        exit(1)

def extractUrlStammdaten(nova_response: VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFile):
    return nova_response.body.get_stammdaten_file_response.stammdaten_file_response.stammdaten_file_path


if __name__ == '__main__':
    #check configuration
    ojp_trip_request_xml=''
    check_configuration()

    # build didok list
    dlist=load_didok_stammdaten()
    # start working
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2"}
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)
    try:
        areqbody='''
  <?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header/>
  <soapenv:Body>
    <vs:getStammdatenFile xmlns:ns22="http://nova.voev.ch/services/internal/leistungnotification" xmlns:ns21="http://nova.voev.ch/services/v14/vertrieb" xmlns:nova-leistungnotiz="http://nova.voev.ch/services/v14/leistungnotiz" xmlns:ns19="http://nova.voev.ch/services/v14/vertrag" xmlns:ns18="http://nova.voev.ch/services/internal" xmlns:vs="http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten" xmlns:nova-protokoll="http://nova.voev.ch/services/v14/vertrieb/protokoll" xmlns:nova-erneuerungsinfo="http://nova.voev.ch/services/v14/vertrieb/erneuerungsinfo" xmlns:ns14="http://nova.voev.ch/services/v14/kuko" xmlns:offlinemanagement="http://nova.voev.ch/services/v14/vertrieb/offlinemanagement" xmlns:nova-monitoring="http://nova.voev.ch/services/internal/monitoring" xmlns:nova-preisauskunft="http://nova.voev.ch/services/v14/preisauskunft" xmlns:vb="http://nova.voev.ch/services/v14/vertriebsbase" xmlns:base="http://nova.voev.ch/services/v14/base" xmlns:ns8="http://nova.voev.ch/services/v14/fachlichervertrag" xmlns:inkasso="http://nova.voev.ch/services/v14/inkasso" xmlns:nova-vertragskonto="http://nova.voev.ch/services/v14/vertragskonto" xmlns:novasp-swisspass="http://nova.voev.ch/services/v14/swisspass" xmlns:novakuko="http://nova.voev.ch/services/v14/kundeninteraktion" xmlns:novagp="http://nova.voev.ch/services/v14/geschaeftspartner" xmlns="http://nova.voev.ch/services/v14/vertrieb" xmlns:novavt-vertrag="http://nova.voev.ch/services/v14/vertragbase">
      <vs:stammdatenFileRequest vs:leistungsVermittler="11" vs:kanalCode="41">
        <vs:correlationKontext>
          <base:correlationId>4fc5e857-33e4-4f0e-be31-a535349003d5</base:correlationId>
          <base:geschaeftsProzessId>512e62f5-6609-4861-b611-9d6f72aedd22</base:geschaeftsProzessId>
        </vs:correlationKontext>
      </vs:stammdatenFileRequest>
    </vs:getStammdatenFile>
  </soapenv:Body>
</soapenv:Envelope>
        '''
        nova_request=parse_nova_stammdaten_request(areqbody)
        nova_request_xml = serializer.render(nova_request)
        log('nova_stammdaten_request.xml', nova_request_xml)
        nova_client = get_nova_client()
        nova_response = nova_client.send(nova_request, headers=headers)
        if nova_response:
            serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
            serializer = XmlSerializer(serializer_config)
            nova_response_xml = serializer.render(nova_response)
            log('nova_stammdaten_response.xml', nova_response_xml)
        # get file from response
        url = extractUrlStammdaten(nova_response)
        r = requests.get(url, allow_redirects=True)
        open(NOVA_STAMMDATEN_FILE,'wb').write(r.content)
        with gzip.open(NOVA_STAMMDATEN_FILE,'rb') as file_in:
            with open(NOVA_STAMMDATEN_FILE_UNZIPPED,'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)
                print ("Stammdaten kopiert")
        tree=ET.parse(NOVA_STAMMDATEN_FILE_UNZIPPED)
        root=tree.getroot()
        a=root.findall('.//{http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten}moeglicherParkplatz')
        b=root.findall('.//{http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten}moeglicheParkplaetze')
        respl={}
        for pl in a:
            bezeichnung=pl.get('{http://nova.voev.ch/services/v14/vertriebsbase}bezeichnung')
            parkplatzCode=pl.get('{http://nova.voev.ch/services/v14/vertriebsbase}parkplatzCode')
            if dlist.get(bezeichnung):
                respl[bezeichnung]=([bezeichnung,parkplatzCode]+dlist[bezeichnung])
            else:
                respl[bezeichnung]=([bezeichnung,parkplatzCode]+["","","","",""])
        for pl in b:
            bezeichnung = pl.get('{http://nova.voev.ch/services/v14/vertriebsbase}bezeichnung')
            parkplatzCode = pl.get('{http://nova.voev.ch/services/v14/vertriebsbase}parkplatzCode')
            if dlist.get(bezeichnung):
                respl[bezeichnung]=([bezeichnung,parkplatzCode]+dlist[bezeichnung])
            else:
                respl[bezeichnung]=([bezeichnung,parkplatzCode]+["","","","",""])
        #write list as csv
        fields=['Bezeichnung','Code','sloid','Didok','offName','lon','lat']
        thelist = respl.items()
        rows =[]
        for l in thelist:
            rows.append(l[1])
        with open(NOVA_PARKPLATZ_FILE,'w',newline='',encoding='utf-8') as f:
            write = csv.writer(f,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
            write.writerow(fields)
            write.writerows(rows)
    except Exception as e:
        # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
        log('error_file.xml', str(e))
        print (str(e))
        print(traceback.format_exc())
