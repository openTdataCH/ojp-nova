#!/usr/bin/env python3

from fastapi import FastAPI, Request, Response, HTTPException
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from map_nova_to_ojp import test_nova_to_ojp
from map_ojp_to_ojp import map_ojp_trip_result_to_ojp_fare_request, parse_ojp
from test_network_flow import test_nova_request_reply, call_ojp_2000

from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG

app = FastAPI(title="OJP2NOVA")

serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer = XmlSerializer(serializer_config)

ns_map = {'': 'http://www.siri.org.uk/siri', 'ojp': 'http://www.vdv.de/ojp'}

@app.post("/"+HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request):
    body = await fastapi_req.body()

    ojp_fare_request = parse_ojp(body.decode('utf-8'))
    if ojp_fare_request.ojprequest:
        if ojp_fare_request.ojprequest.service_request.ojpfare_request:
            nova_response = test_nova_request_reply(ojp_fare_request)
            if nova_response:
                ojp_fare_result = test_nova_to_ojp(nova_response)
                ojp_fare_result_xml = serializer.render(ojp_fare_result, ns_map=ns_map)
                return Response(ojp_fare_result_xml, media_type="application/xml; charset=utf-8")

            # TODO: In band error error reply?
            raise HTTPException(status_code=400, detail="There was no NOVA response")

        else:
            return Response(call_ojp_2000(body.decode('utf-8')), media_type="application/xml; charset=utf-8")

    else:
        # TODO: In band error error reply?
        raise HTTPException(status_code=400, detail="There was no OJP request")

if __name__ == "__main__":
    import uvicorn
    if (HTTPS):
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
