#!/usr/bin/env python3
import datetime

from fastapi import FastAPI, Request, Response, HTTPException
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from map_nova_to_ojp import test_nova_to_ojp
from map_ojp_to_ojp import parse_ojp
from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, \
    OtherError, OjpfareDelivery
from test_network_flow import test_nova_request_reply, call_ojp_2000

from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG

app = FastAPI(title="OJP2NOVA")

serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer = XmlSerializer(serializer_config)

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

def error_response(error_text:str):
    return Ojp(ojpresponse=
        Ojpresponse(service_delivery=
                    ServiceDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.datetime.utcnow()),
                                    producer_ref="OJP2NOVA",
                                    error_condition=ServiceDeliveryStructure.ErrorCondition(other_error=OtherError(error_text)))))

@app.post("/"+HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request):
    body = await fastapi_req.body()

    ojp_fare_request = parse_ojp(body.decode('utf-8'))
    if ojp_fare_request.ojprequest:
        if ojp_fare_request.ojprequest.service_request.ojpfare_request:
            nova_response = test_nova_request_reply(ojp_fare_request)
            if nova_response:
                ojp_fare_delivery = test_nova_to_ojp(nova_response)
                if ojp_fare_delivery:
                    xml = serializer.render(Ojp(ojpresponse=
                                                Ojpresponse(service_delivery=
                                                            ServiceDelivery(response_timestamp=ojp_fare_delivery.response_timestamp,
                                                                            producer_ref="OJP2NOVA",
                                                                            ojpfare_delivery=[ojp_fare_delivery]))), ns_map=ns_map)
                    return Response(xml, media_type="application/xml; charset=utf-8")
                else:
                    return Response(serializer.render(error_response("There was a NOVA response, but it cannot be used"), ns_map=ns_map),
                                    status_code=400, media_type="application/xml; charset=utf-8")

            return Response(serializer.render(error_response("There was no NOVA response"), ns_map=ns_map), status_code=400, media_type="application/xml; charset=utf-8")

        else:
            return Response(call_ojp_2000(body.decode('utf-8')), media_type="application/xml; charset=utf-8")

    else:
        return Response(serializer.render(error_response("There was no (valid) OJP request"), ns_map=ns_map), status_code=400,
                        media_type="application/xml; charset=utf-8")

if __name__ == "__main__":
    import uvicorn
    if (HTTPS):
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
