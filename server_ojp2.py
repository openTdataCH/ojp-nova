#!/usr/bin/env python3
import datetime

from fastapi import FastAPI, Request, Response, HTTPException
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from map_nova_to_ojp2 import test_nova_to_ojp2
from map_ojp2_to_ojp2 import parse_ojp2
from support import error_response

from ojp2 import (
    Ojp,
    Ojpresponse,
    ServiceDelivery,
    ServiceDeliveryStructure,
    OtherError,
    OjpfareDelivery,
    ParticipantRefStructure,
)
from test_network_flow import call_ojp_20, test_nova_request_reply_for_ojp2
from configuration import (
    HTTP_HOST,
    HTTP_PORT,
    HTTPS,
    SSL_CERTFILE,
    SSL_KEYFILE,
    HTTP_SLUG,

)
import logger

# from support import add_error_response

app = FastAPI(title="OJP2TONOVA")

serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer = XmlSerializer(config=serializer_config)

ns_map = {"": "http://www.siri.org.uk/siri", "ojp": "http://www.vdv.de/ojp"}


@app.post("/" + HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request) ->Response:
    body = await fastapi_req.body()
    logger.log_entry("Received request: " + str(body))

    ojp_fare_request = None
    error = None
    try:
        ojp_fare_request = parse_ojp2(body.decode("utf-8"))
    except Exception as e:
        error = e

    try:
        if ojp_fare_request and ojp_fare_request.ojprequest:
            # a request was made and it seems legit
            if ojp_fare_request.ojprequest.service_request.ojpfare_request:
                # we deal with a OJPFare Request and will ask NOVA
                logger.log_entry("Query to NOVA: " + str(ojp_fare_request))
                nova_response = test_nova_request_reply_for_ojp2(ojp_fare_request)
                if nova_response:
                    # we got a valid response
                    ojp_fare_delivery = test_nova_to_ojp2(nova_response)
                    if ojp_fare_delivery:
                        # we have a OJPFareDelivery to work with
                        # we add the warnings
                        logger.log_entry(
                            "Workable NOVA response put into OJP: "
                            + str(ojp_fare_delivery)
                        )
                        # ojp_fare_delivery=add_error_response(ojp_fare_delivery)
                        xml = serializer.render(
                            Ojp(
                                ojpresponse=Ojpresponse(
                                    service_delivery=ServiceDelivery(
                                        response_timestamp=ojp_fare_delivery.response_timestamp,
                                        producer_ref=ParticipantRefStructure(
                                            value="OJP2NOVA"
                                        ),
                                        ojpfare_delivery=[ojp_fare_delivery],
                                    )
                                )
                            ),
                            ns_map=ns_map,
                        )
                        return Response(
                            xml, media_type="application/xml; charset=utf-8"
                        )
                    else:
                        logger.log_entry(
                            "There was a NOVA response, but it can't be used:"
                            + str(nova_response)
                        )
                        return Response(
                            serializer.render(
                                error_response(
                                    "There was a NOVA response, but it cannot be used"
                                ),
                                ns_map=ns_map,
                            ),
                            status_code=400,
                            media_type="application/xml; charset=utf-8",
                        )
                logger.log_entry("There was no NOVA response")
                return Response(
                    serializer.render(
                        error_response("There was no NOVA response"), ns_map=ns_map
                    ),
                    status_code=400,
                    media_type="application/xml; charset=utf-8",
                )
            else:
                logger.log_entry(
                    "Returning the call to the OJP server:" + str(body.decode("utf-8"))
                )
                s, r = call_ojp_20(body.decode("utf-8"))
                return Response(
                    r, media_type="application/xml; charset=utf-8", status_code=s
                )
        else:
            # very general errors
            if error:
                # an error message was provided in the exception
                logger.log_entry("Couldn't extract a valid OJP request")
                return Response(
                    serializer.render(
                        error_response(
                            "There was no (valid) OJP request\n" + str(error)
                        ),
                        ns_map=ns_map,
                    ),
                    status_code=400,
                    media_type="application/xml; charset=utf-8",
                )
            else:
                # no error message was provided in the exception
                logger.log_entry("No valid OJP request")
                return Response(
                    serializer.render(
                        error_response("There was no (valid) OJP request"),
                        ns_map=ns_map,
                    ),
                    status_code=400,
                    media_type="application/xml; charset=utf-8",
                )
    except Exception as e:
        # not yet really sophisticated handling of all other errors during the work (should be regular OJPDeliveries with OtherError set
        logger.log_entry("Some other error occured: " + str(e))
        return Response(
            serializer.render(error_response(str(e)), ns_map=ns_map),
            status_code=400,
            media_type="application/xml; charset=utf-8",
        )


if __name__ == "__main__":
    import uvicorn

    if HTTPS:
        uvicorn.run(
            app,
            host=HTTP_HOST,
            port=HTTP_PORT,
            ssl_keyfile=SSL_KEYFILE,
            ssl_certfile=SSL_CERTFILE,
        )
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
