#!/usr/bin/env python3

import json
import traceback
from typing import Tuple, Any, Optional

import requests
import urllib3
from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import ojp.fare_result_structure
from api.errors.NoNovaResponseError import NoNovaResponseError
from configuration import *
from support import OJPError
from test_create_ojp_request import *
from map_nova_to_ojp import test_nova_to_ojp
from map_nova_to_ojp2 import test_nova_to_ojp2

from map_ojp_to_nova import test_ojp_fare_request_to_nova_request
from map_ojp2_to_nova import test_ojp2_fare_request_to_nova_request

from map_ojp_to_ojp import parse_ojp, map_ojp_trip_result_to_ojp_fare_request #, map_ojp_trip_result_to_ojp_refine_request
from map_ojp2_to_ojp2 import parse_ojp2, map_ojp2_trip_result_to_ojp2_fare_request #, map_ojp_trip_result_to_ojp_refine_request

from nova import PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft, \
    PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput
from ojp2 import Ojp as Ojp2
from ojp import Ojp, OjpfareDelivery
from xslt_transform import transform_xml, is_version_2_0
import xml_logger
import logging

logger = logging.getLogger(__name__)

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}


def call_ojp_2000(request_body:str) -> Tuple[int,str]:
    try:
        access_token = OJP_TOKEN
        headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/xml; charset=utf-8' }
        api_call_response = requests.post(OJP_URL_API, data=request_body.encode('utf-8'), headers=headers, verify=False)
        api_call_response.encoding = api_call_response.apparent_encoding
        return api_call_response.status_code,api_call_response.text

    except Exception as e:
        message = 'Failed: {:s}.'.format(str(e))
        raise IOError(message, e)


def call_ojp_20(request_body:str) -> Tuple[int,str]:
    try:
        access_token = OJP_2_TOKEN
        headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/xml; charset=utf-8' }
        api_call_response = requests.post(OJP_2_URL_API, data=request_body.encode('utf-8'), headers=headers, verify=False)
        api_call_response.encoding = api_call_response.apparent_encoding
        return api_call_response.status_code,api_call_response.text

    except Exception as e:
        message = 'Failed: {:s}.'.format(str(e))
        raise IOError(message, e)

class OAuth2Helper:
    # Credits: https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code

    def __init__(self, client_id:str, client_secret:str, scope:str):
        urllib3.disable_warnings()
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.current_token = None

    def get_token(self, new_token:bool=False) ->Any:
        if new_token or not self.current_token:
            data = {'grant_type': 'client_credentials', 'scope': self.scope}
            access_token_response = requests.post(NOVA_TOKEN_URL, data=data, verify=False, allow_redirects=False,
                                                  auth=(self.client_id, self.client_secret))
            self.current_token = json.loads(access_token_response.text)
        if self.current_token is None:
            return None
        return self.current_token['access_token']

def get_nova_client() -> Client:
    # TODO: It might be more elegant to cache this client in some way, but we would need to handle the expiry of the token
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET, scope=NOVA_SCOPE)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2" }

    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(config)
    location = NOVA_BASE_URL + NOVA_PREISAUSKUNFT_PATH
    client = Client.from_service(PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft, location=location, encoding="utf-8")
    client.parser = parser

    return client

def test_nova_request_reply(ojp: Ojp)->Optional[PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput]:
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET, scope=NOVA_SCOPE)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2"}
    nova_request = test_ojp_fare_request_to_nova_request(ojp)
    nova_client = get_nova_client()
    nova_response :Optional[PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput] = nova_client.send(nova_request, headers=headers)
    if nova_response is None:
        raise NoNovaResponseError()
    xml_logger.log_object_as_xml('nova_response.xml',nova_response)
    return nova_response



def test_nova_request_reply_for_ojp2(ojp: Ojp2)->Optional[PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput]:
    oauth_helper = OAuth2Helper(client_id=NOVA_CLIENT_ID, client_secret=NOVA_CLIENT_SECRET, scope=NOVA_SCOPE)
    access_token = oauth_helper.get_token()
    headers = {'Authorization': 'Bearer ' + access_token, "User-Agent": "OJP2NOVA/0.2"}
    nova_request = test_ojp2_fare_request_to_nova_request(ojp)
    nova_client = get_nova_client()
    nova_response : PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput = nova_client.send(nova_request, headers=headers)
    if nova_response is None:
        raise NoNovaResponseError()
    xml_logger.log_object_as_xml('nova_response.xml',nova_response)
    return nova_response

def check_configuration() ->None:
    if (len(NOVA_CLIENT_SECRET)==0):
        logger.error("Nova client secret not set in the configuration")
        exit(1)

if __name__ == '__main__':
    #check configuration
    ojp_trip_request_xml=''
    check_configuration()
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=serializer_config)
    for rf in READFILE:
        if (not READTRIPREQUESTFILE):
            ojp_trip_request = test_create_ojp_trip_request_simple_1()
            ojp_trip_request_xml = serializer.render(ojp_trip_request, ns_map=ns_map)
        else:
            inputfile = open(rf, 'r', encoding='utf-8')
            ojp_trip_request_xml = inputfile.read()
            inputfile.close()
        xml_logger.log_serialized('ojp_trip_request.xml', ojp_trip_request_xml)
        try:
            print (f"\n********************************************\n{rf}\n********************************************\n")
            if  is_version_2_0(ojp_trip_request_xml):
                #We process an OJP 2 request
                status, r = call_ojp_20(ojp_trip_request_xml)
                if status != 200:
                    message = f"call returned a wrong status {status}"
                    raise IOError(message)
                ojp_trip_result = parse_ojp2(r)
                ojp_trip_result_xml = serializer.render(ojp_trip_result, ns_map=ns_map)
                xml_logger.log_serialized('ojp_trip_reply.xml', ojp_trip_result_xml)
                ojp_fare_request = map_ojp2_trip_result_to_ojp2_fare_request(ojp_trip_result)
                if ojp_fare_request is None:
                    raise OJPError("ERR102: No fare request could be generated from trip delivery.")
                else:
                    ojp_fare_request_xml = serializer.render(ojp_fare_request, ns_map=ns_map)
                xml_logger.log_serialized('ojp_fare_request.xml', ojp_fare_request_xml)
                nova_response = test_nova_request_reply_for_ojp2(ojp_fare_request)
                if nova_response:
                    ojp_fare_result = test_nova_to_ojp2(nova_response)
                    if not(ojp_fare_result):
                        ojp_fare_result_xml="Not a valid nova fare response received." #TODO Improve with better handling
                        xml_logger.log_serialized('ojp_fare_result.xml', ojp_fare_result_xml)
                    else:
                        ojp_fare_result_xml = serializer.render(ojp_fare_result, ns_map=ns_map)
                        for fr1 in ojp_fare_result.fare_result:
                            for fr in fr1.trip_fare_result:
                                print("Legs: " + str(fr.from_leg_id_ref) + "-" + str(fr.to_leg_id_ref))
                                print(fr.fare_product)
                                print("\n")
                        xml_logger.log_serialized('ojp_fare_result.xml', ojp_fare_result_xml)


            else:
                # We work on a OJP 1.0 request
                status,r = call_ojp_2000(ojp_trip_request_xml)
                if status != 200:
                    message = f"call returned a wrong status {status}:\n{r}"
                    raise IOError(message)
                ojp_trip_result1 = parse_ojp(r)
                ojp_trip_result_xml1 = serializer.render(ojp_trip_result1, ns_map=ns_map)
                xml_logger.log_serialized('ojp_trip_reply.xml', ojp_trip_result_xml1)
                ojp_fare_request1 = map_ojp_trip_result_to_ojp_fare_request(ojp_trip_result1)
                ojp_fare_request_xml1 = serializer.render(ojp_fare_request1, ns_map=ns_map)
                xml_logger.log_serialized('ojp_fare_request.xml', ojp_fare_request_xml1)

                if ojp_fare_request1 :
                    nova_response1 = test_nova_request_reply(ojp_fare_request1)
                else:
                    nova_response1 = None
                if nova_response1:
                    ojp_fare_result1 : OjpfareDelivery = test_nova_to_ojp(nova_response1)
                    ojp_fare_result_xml1 = serializer.render(ojp_fare_result1, ns_map=ns_map)
                    if ojp_fare_result1 is None:
                        raise OJPError("ERR100: No OJP Fare result obtained.")
                    for fr in ojp_fare_result1.fare_result:
                        for fr1 in fr.trip_fare_result:
                            print("Legs: " + str(fr1.from_trip_leg_id_ref) + "-" + str(fr1.to_trip_leg_id_ref))
                            print(fr1.fare_product)
                            print("\n")
                    xml_logger.log_serialized('ojp_fare_result.xml', ojp_fare_result_xml1)


        except Exception as e:
            # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
            logger.exception(e)
            xml_logger.log_serialized('error_file.xml', str(e))
            traceback.print_exc()


