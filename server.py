#!/usr/bin/env python3
import datetime

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from map_nova_to_ojp import test_nova_to_ojp
from map_ojp_to_ojp import map_ojp_trip_result_to_ojp_fare_request, parse_ojp
from support import error_response
from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, \
    OtherError, OjpfareDelivery
from test_network_flow import test_nova_request_reply, call_ojp_2000
from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG, VATRATE
import logger
#from support import add_error_response

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

app = FastAPI(title="OJP2NOVA")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
	allow_headers=["*"],
    max_age=3600,
)

serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer = XmlSerializer(serializer_config)

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}


@app.post("/"+HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request):
    body = await fastapi_req.body()
    logger.log_entry("Received request: " + str(body))

    body_str = body.decode('utf-8')
    
    is_ojp_trip_request_response = _is_ojp_trip_request_response(body_str)
    if is_ojp_trip_request_response:
        ojp_fare_request = map_ojp_trip_result_to_ojp_fare_request(parse_ojp(body_str))
        body_str = serializer.render(ojp_fare_request, ns_map=ns_map)

    ojp_fare_request = None
    error = None
    try:
        ojp_fare_request = parse_ojp(body_str)
    except Exception as e:
        error = e

    try:
        if ojp_fare_request and ojp_fare_request.ojprequest:
            # a request was made and it seems legit
            if ojp_fare_request.ojprequest.service_request.ojpfare_request:
                # we deal with a OJPFare Request andn will ask NOVA
                logger.log_entry("Query to NOVA: "+str(ojp_fare_request))
                nova_response = test_nova_request_reply(ojp_fare_request)
                if nova_response:
                    #we got a valid response
                    ojp_fare_delivery = test_nova_to_ojp(nova_response)
                    if ojp_fare_delivery:
                        # we have a OJPFareDelivery to work with
                        # we add the warnings
                        logger.log_entry("Workable NOVA response put into OJP: "+str(ojp_fare_delivery))
                        # ojp_fare_delivery=add_error_response(ojp_fare_delivery)
                        xml = serializer.render(Ojp(ojpresponse=   Ojpresponse(service_delivery=  ServiceDelivery(response_timestamp=ojp_fare_delivery.response_timestamp,producer_ref="OJP2NOVA",
ojpfare_delivery=[ojp_fare_delivery]))), ns_map=ns_map)
                        return Response(xml, media_type="application/xml; charset=utf-8")
                    else:
                        logger.log_entry("There was a NOVA response, but it can't be used:"+ str(nova_response))
                        return Response(serializer.render(error_response("There was a NOVA response, but it cannot be used"), ns_map=ns_map),
                                        status_code=400, media_type="application/xml; charset=utf-8")
                logger.log_entry("There was no NOVA response")
                return Response(serializer.render(error_response("There was no NOVA response"), ns_map=ns_map), status_code=400, media_type="application/xml; charset=utf-8")
            else:
                logger.log_entry("Returning the call to the OJP server:"+str(body.decode('utf-8')))
                return Response(call_ojp_2000(body.decode('utf-8')), media_type="application/xml; charset=utf-8")
        else:
            #very general errors
            if error:
              # an error message was provided in the exception
              logger.log_entry("Couldn't extract a valid OJP request")
              return Response(serializer.render(error_response("There was no (valid) OJP request\n"+str(error)), ns_map=ns_map), status_code=400,
                            media_type="application/xml; charset=utf-8")
            else:
                # no error message was provided in the exception
                logger.log_entry("No valid OJP request")
                return Response(serializer.render(error_response("There was no (valid) OJP request"), ns_map=ns_map), status_code=400,
                            media_type="application/xml; charset=utf-8")
    except Exception as e:
        # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
        logger.log_entry("Some other error occured.")
        return Response(
            serializer.render(error_response(str(e)), ns_map=ns_map),
            status_code=400,
            media_type="application/xml; charset=utf-8")

def _is_ojp_trip_request_response(xml_str: str) -> bool:
    config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )

    parser = XmlParser(config)
    ojp_data = parser.from_string(xml_str)

    if ojp_data and ojp_data.ojpresponse and ojp_data.ojpresponse.service_delivery:
        return ojp_data.ojpresponse.service_delivery.ojptrip_delivery is not None

    return False

if __name__ == "__main__":
    import uvicorn
    if (HTTPS):
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
