#!/usr/bin/env python3

from fastapi import FastAPI, Request, Response
from api.FareServiceOjp1 import FareServiceOjp1
from configuration import HTTP_HOST, HTTP_PORT, HTTPS, SSL_CERTFILE, SSL_KEYFILE, HTTP_SLUG
import logging
import app_logging

# from support import add_error_response

app_logging.setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="OJPTONOVA")

fare_service = FareServiceOjp1()

@app.post("/" + HTTP_SLUG, tags=["Open Journey Planner"])
async def post_request(fastapi_req: Request) ->Response:
    body = await fastapi_req.body()
    logger.debug("Received request: " + str(body))
    return fare_service.handle_request(body)

if __name__ == "__main__":
    import uvicorn

    if HTTPS:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT, ssl_keyfile=SSL_KEYFILE, ssl_certfile=SSL_CERTFILE)
    else:
        uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
