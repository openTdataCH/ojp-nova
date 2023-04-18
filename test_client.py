#!/usr/bin/env python3

import requests
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from create_ojp_request import test_create_ojp_trip_request
from map_ojp_to_ojp import map_ojp_trip_result_to_ojp_fare_request, parse_ojp

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

if __name__ == '__main__':
    ojp_trip_request = test_create_ojp_trip_request()
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)
    ojp_trip_request_xml = serializer.render(ojp_trip_request, ns_map=ns_map)
    r = requests.post("http://127.0.0.1:8000/ojp2023", data=ojp_trip_request_xml.encode("utf-8"), verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)

    ojp_trip_result = parse_ojp(r.text)
    ojp_fare_request = map_ojp_trip_result_to_ojp_fare_request(ojp_trip_result)
    ojp_fare_request_xml = serializer.render(ojp_fare_request, ns_map=ns_map)
    r = requests.post("http://127.0.0.1:8000/ojp2023", data=ojp_fare_request_xml.encode("utf-8"), verify=False)
    r.encoding = r.apparent_encoding
    print(r.text)
