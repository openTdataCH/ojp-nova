#!/usr/bin/env python3

from fastapi import FastAPI, Request, Response

from api.OjpVersionParser import OjpVersionParser
from api.ojp1.FareServiceOjp1 import FareServiceOjp1
from api.ojp2.FareServiceOjp2 import FareServiceOjp2
from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG
import logging
import app_logging

app_logging.setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="OJPTONOVA")
fare_service1 = FareServiceOjp1()

# implements basic liveness probe
@app.get("/health/liveness", tags=["Health"])
async def liveness(fastapi_req: Request):
    return Response("Liveness: OK", media_type="text/plain; charset=utf-8")

# implements basic readiness probe
@app.get("/health/readiness", tags=["Health"])
async def readiness(fastapi_req: Request):
    return Response("Readiness: OK", media_type="text/plain; charset=utf-8")

@app.post("/" + HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request) ->Response:
    body = await fastapi_req.body()
    logger.debug("Received request: " + str(body))
    return fare_service1.handle_request(body)

if __name__ == "__main__":
    import uvicorn

    if HTTPS:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
