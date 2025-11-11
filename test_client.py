#!/usr/bin/env python3
from time import sleep

import requests
from configuration import *
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from test_create_ojp_request import test_create_ojp_trip_request_simple_3
from map_ojp_to_ojp import map_ojp_trip_result_to_ojp_fare_request, parse_ojp

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

if __name__ == '__main__':

    for i in range(600):
        try:
            ojp_trip_request = test_create_ojp_trip_request_simple_3()
            serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
            serializer = XmlSerializer(config=serializer_config)

            if (HTTPS):
                if HTTP_PORT == '':
                    url = f"https://{HTTP_HOST}/{HTTP_SLUG}"
                else:
                    url = f"https://{HTTP_HOST}:{HTTP_PORT}/{HTTP_SLUG}"
            else:
                url = f"http://{HTTP_HOST}:{HTTP_PORT}/{HTTP_SLUG}"
            access_token = OJP_FARE_TOKEN
            headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/xml; charset=utf-8'}

            ojp_trip_request_xml = serializer.render(ojp_trip_request, ns_map=ns_map)
            r = requests.post(url, data=ojp_trip_request_xml.encode("utf-8"), headers=headers, verify=False)
            r.encoding = r.apparent_encoding
            print(r.text)
            sleep(1)
            ojp_trip_result = parse_ojp(r.text)
            ojp_fare_request = map_ojp_trip_result_to_ojp_fare_request(ojp_trip_result)
            ojp_fare_request_xml = serializer.render(ojp_fare_request, ns_map=ns_map)
            r = requests.post(url, data=ojp_fare_request_xml.encode("utf-8"), headers=headers, verify=False)
            r.encoding = r.apparent_encoding
            print(r.text)
        except Exception as e:
            print(str(e))




    # faulty file sent to OJPFare must be handled gracefully
    print("Testing faulty OJPFare request")
    ojp_fare_request_xml = "<xml></xml>"
    r = requests.post(url, data=ojp_fare_request_xml.encode("utf-8"), headers=headers,  verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)

