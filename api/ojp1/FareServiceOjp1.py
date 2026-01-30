import logging

from fastapi import Response

from api.ErrorHandler import ErrorHandler
from api.FareService import FareService
from api.SerializerUtil import SerializerUtil
from api.errors.ApiError import ApiError
from api.errors.InvalidOjpRequestError import InvalidOjpRequestError
from api.errors.OjpRequestParseError import OjpRequestParseError
from api.ojp1.ErrorResponseProviderOjp1 import ErrorResponseProviderOjp1
from map_nova_to_ojp import map_nova_reply_to_ojp_fare_delivery
from map_ojp_to_ojp import parse_ojp
from ojp import OjpfareDelivery, Ojpresponse, ServiceDelivery, Ojp
from test_network_flow import test_nova_request_reply,call_ojp_2000


class FareServiceOjp1(FareService):
    def __init__(self, *args, **kwargs) -> None:
        self.logger = logging.getLogger(__name__)
        super().__init__(*args, **kwargs)

    def handle_request(self, body: bytes) -> Response:
        error_handler = ErrorHandler(ErrorResponseProviderOjp1())
        try:
            ojp_fare_request = _parse_request(body)
            _validate_request(ojp_fare_request)

            if ojp_fare_request.ojprequest.service_request.ojpfare_request:
                self.logger.debug("Query to NOVA: " + str(ojp_fare_request))
                nova_response = test_nova_request_reply(ojp_fare_request)


                ojp_fare_delivery = map_nova_reply_to_ojp_fare_delivery(nova_response)

                self.logger.debug("Workable NOVA response put into OJP: " + str(ojp_fare_delivery))
                return _create_response(ojp_fare_delivery)
            else:
                self.logger.debug("Returning the call to the OJP server:" + str(body.decode("utf-8")))
                s, r = call_ojp_2000(body.decode("utf-8"))
                return Response(r, media_type="application/xml; charset=utf-8", status_code=s)

        except ApiError as error:
            return error_handler.handle_error(error)


def _validate_request(ojp_fare_request: Ojp):
    if ojp_fare_request.ojprequest is None:
        raise InvalidOjpRequestError(message="missing Element OJPRequest.");

    if ojp_fare_request.ojprequest.service_request.ojpfare_request is None:
        raise InvalidOjpRequestError()


def _parse_request(body: bytes) -> Ojp:
    try:
        return parse_ojp(body.decode("utf-8"))
    except Exception as e:
        raise OjpRequestParseError(cause=e)


def _create_response(ojp_fare_delivery: OjpfareDelivery) -> Response:
    xml = SerializerUtil.serializer.render(
        Ojp(
            ojpresponse=Ojpresponse(
                service_delivery=ServiceDelivery(
                    response_timestamp=ojp_fare_delivery.response_timestamp,
                    producer_ref="OJP2NOVA",
                    ojpfare_delivery=[ojp_fare_delivery],
                )
            )
        ),
        ns_map=SerializerUtil.ns_map,
    )
    return Response(xml, media_type="application/xml; charset=utf-8")
