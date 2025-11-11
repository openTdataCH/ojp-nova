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
from xml.dom.minidom import parseString

import xml_logger
from configuration import *
from test_create_ojp_request import *
from map_nova_to_ojp import test_nova_to_ojp
from map_nova_to_ojp2 import test_nova_to_ojp2

from map_ojp_to_nova import test_ojp_fare_request_to_nova_request
from map_ojp2_to_nova import test_ojp2_fare_request_to_nova_request

from map_ojp_to_ojp import parse_ojp, map_ojp_trip_result_to_ojp_fare_request #, map_ojp_trip_result_to_ojp_refine_request
from map_ojp2_to_ojp2 import parse_ojp2, map_ojp2_trip_result_to_ojp2_fare_request #, map_ojp_trip_result_to_ojp_refine_request

from nova import PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft
from ojp import Ojp
from xslt_transform import transform_xml, is_version_2_0
ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}




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





def check_configuration():
    if (len(NOVA_CLIENT_SECRET)==0):
        print("Secrets not set in the configuration")
        exit(1)


def send_nova(url: str, headers: dict, xml_body: str) -> requests.Response:
    """
    Sends an XML request to the specified URL with the given headers.

    :param url: The URL to which the request is sent.
    :param headers: A dictionary of headers to include in the request.
    :param xml_body: The XML body of the request as a string.
    :return: The response from the server.
    """
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, data=xml_body)

        # Raise an exception for HTTP error responses
        response.raise_for_status()

        return response  # Return the response object

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Handle other errors

    return None  # Return None if there was an error
if __name__ == '__main__':
    check_configuration()
    # read NOVA request file

    READFILE="generated/nova_request.xml"
    print(f'Processing {READFILE}\n\n')
    with open(READFILE, 'r', encoding='utf-8') as inputfile:
        nova_request = inputfile.read()
    # send it to NOVA
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token,
               'SOAPAction': 'http://nova.voev.ch/services/v14/preisauskunft/erstellePreisAuskunft',
               'Content-Type':'text/xml; charset=utf-8',
               "User-Agent": "OJP2NOVA/0.2" }

    nova_response=send_nova(NOVA_URL_API, headers, nova_request)
    if nova_response:
        #serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
        #serializer = XmlSerializer(config=serializer_config)
        #nova_response_xml = serializer.render(nova_response)
        dom=parseString(nova_response.text)
        pretty_xml=dom.toprettyxml(indent="  ")
        xml_logger.log_serialized('generated/nova_response_direct.xml',pretty_xml)



