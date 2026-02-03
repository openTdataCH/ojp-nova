#!/usr/bin/env python3

import logging

from fastapi import FastAPI, Request, Response

import app_logging
from api.OjpVersionParser import OjpVersionParser
from api.ojp1.OjpFareServiceOjp1 import FareServiceOjp1
from api.ojp2.OjpFareServiceOjp2 import FareServiceOjp2
from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG

app_logging.setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="OJPTONOVA")

fare_service1 = FareServiceOjp1()
fare_service2 = FareServiceOjp2()

version_parser = OjpVersionParser()

@app.get("/health/liveness", tags=["Health"])
async def liveness(fastapi_req: Request):
    """
    Implements liveness probe.
    """
    return Response("Liveness: OK", media_type="text/plain; charset=utf-8")

@app.get("/health/readiness", tags=["Health"])
async def readiness(fastapi_req: Request):
    """
    Implements readiness probe.
    """
    return Response("Readiness: OK", media_type="text/plain; charset=utf-8")

@app.post("/" + HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request) ->Response:
    """
    Handles OjpFare requests: for ojp1 or ojp2.
    """
    body = await fastapi_req.body()
    logger.debug("Received request: " + str(body))

    version = version_parser.parse_version(str(body))
    if version == "1.0":
        return fare_service1.handle_request(body)
    else:
        return fare_service2.handle_request(body)

if __name__ == "__main__":
    import uvicorn

    if HTTPS:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
