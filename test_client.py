#!/usr/bin/env python3

import requests
from configuration import *
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from test_create_ojp_request import test_create_ojp_trip_request_simple_3
from map_ojp_to_ojp import map_ojp_trip_result_to_ojp_fare_request, parse_ojp

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

if __name__ == '__main__':
    ojp_trip_request = test_create_ojp_trip_request_simple_3()
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)
    if (HTTPS):
        url="https://"+HTTP_HOST+":"+str(HTTP_PORT)+"/"+HTTP_SLUG
    else:
        url="http://"+HTTP_HOST+":"+str(HTTP_PORT)+"/"+HTTP_SLUG
    ojp_trip_request_xml = serializer.render(ojp_trip_request, ns_map=ns_map)
    r = requests.post(url, data=ojp_trip_request_xml.encode("utf-8"), verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)

    ojp_trip_result = parse_ojp(r.text)
    ojp_fare_request = map_ojp_trip_result_to_ojp_fare_request(ojp_trip_result)
    ojp_fare_request_xml = serializer.render(ojp_fare_request, ns_map=ns_map)
    r = requests.post(url, data=ojp_fare_request_xml.encode("utf-8"), verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)

    # faulty file sent to OJPFare must be handled gracefully
    print("Testing faulty OJPFare request")
    ojp_fare_request_xml = "<xml></xml>"
    r = requests.post(url, data=ojp_fare_request_xml.encode("utf-8"), verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)

