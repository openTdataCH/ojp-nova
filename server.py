#!/usr/bin/env python3

import logging

from fastapi import FastAPI, Request, Response

import app_logging
from api.ojp1 import FareServiceOjp1
from api.ojp2 import FareServiceOjp2
from api.versions import OjpVersionParser

from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG

app_logging.setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="ojp-fare API for OJP1 and OJP2")

fare_service1 = FareServiceOjp1()
fare_service2 = FareServiceOjp2()

version_parser = OjpVersionParser()

@app.get("/health/liveness", tags=["Health"])
async def liveness(fastapi_req: Request):
    """
    Implements liveness probe.
    """
    logger.debug("Received liveness probe request: " + str(fastapi_req))
    return Response("Liveness: OK", media_type="text/plain; charset=utf-8")

@app.get("/health/readiness", tags=["Health"])
async def readiness(fastapi_req: Request):
    """
    Implements readiness probe.
    """
    logger.debug("Received readiness probe request: " + str(fastapi_req))
    return Response("Readiness: OK", media_type="text/plain; charset=utf-8")

@app.post("/" + HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request) ->Response:
    """
    Handles OjpFare requests: for ojp1 or ojp2.
    """
    body = await fastapi_req.body()
    logger.debug("Received request: " + str(body))

    version = version_parser.parse_version(body.decode("utf-8"))
    logger.debug("Received version: " + str(version))
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
