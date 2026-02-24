import datetime
import logging

from fastapi import Response
from xsdata.models.datatype import XmlDateTime

from api.common import OjpFareService, ns_map, serializer
from api.errors import (
    ApiError,
    ErrorHandler,
    ErrorResponseContentProvider,
    InvalidOjpRequestError,
    OjpRequestParseError,
)
from map_nova_to_ojp2 import map_nova_reply_to_ojp_fare_delivery
from map_ojp2_to_ojp2 import parse_ojp2
from ojp2 import (
    Ojp,
    OjpfareDelivery,
    Ojpresponse,
    OtherError,
    ParticipantRefStructure,
    ResponseTimestamp,
    ServiceDelivery,
    ServiceDeliveryStructure,
)
from test_network_flow import call_ojp_20, test_nova_request_reply_for_ojp2


class FareServiceOjp2(OjpFareService):
    def __init__(self, *args, **kwargs) -> None:
        self.logger = logging.getLogger(__name__)
        super().__init__(*args, **kwargs)

    def handle_request(self, body: bytes) -> Response:
        """
        Handles an ojp2 request.
        """
        error_handler = ErrorHandler(ErrorResponseContentProviderOjp2())
        try:
            ojp_fare_request = _parse_request(body)
            _validate_request(ojp_fare_request)
            self.logger.debug("Request passed validation: " + str(ojp_fare_request))

            if ojp_fare_request.ojprequest.service_request.ojpfare_request:
                self.logger.debug(
                    "Fare request - about to query NOVA: " + str(ojp_fare_request)
                )
                nova_response = test_nova_request_reply_for_ojp2(ojp_fare_request)
                ojp_fare_delivery = map_nova_reply_to_ojp_fare_delivery(nova_response)
                self.logger.debug(
                    "Workable NOVA response put into OJP: " + str(ojp_fare_delivery)
                )
                return _create_response(ojp_fare_delivery)
            else:
                self.logger.debug(
                    "OJP request - returning the call to the OJP server:"
                    + str(body.decode("utf-8"))
                )
                s, r = call_ojp_20(body.decode("utf-8"))
                return Response(
                    r, media_type="application/xml; charset=utf-8", status_code=s
                )

        except ApiError as error:
            return error_handler.handle_error(error)


def _validate_request(ojp_fare_request: Ojp):
    if ojp_fare_request.ojprequest is None:
        raise InvalidOjpRequestError(message="missing Element OJPRequest.")

    if ojp_fare_request.ojprequest.service_request.ojpfare_request is None:
        raise InvalidOjpRequestError()


def _parse_request(body: bytes) -> Ojp:
    try:
        return parse_ojp2(body.decode("utf-8"))
    except Exception as e:
        raise OjpRequestParseError(cause=e)


def _create_response(ojp_fare_delivery: OjpfareDelivery) -> Response:
    xml = serializer.render(
        Ojp(
            ojpresponse=Ojpresponse(
                service_delivery=ServiceDelivery(
                    response_timestamp=ojp_fare_delivery.response_timestamp,
                    producer_ref=ParticipantRefStructure(value="OJP2NOVA"),
                    ojpfare_delivery=[ojp_fare_delivery],
                )
            )
        ),
        ns_map=ns_map,
    )
    return Response(xml, media_type="application/xml; charset=utf-8")


class ErrorResponseContentProviderOjp2(ErrorResponseContentProvider):
    ns_map = ns_map
    serializer = serializer

    def provide_error_response_content(self, message: str) -> str:
        """
        Provides the ojp2 error response content for the given error message.
        """
        ojp = Ojp(
            ojpresponse=Ojpresponse(
                service_delivery=ServiceDelivery(
                    response_timestamp=ResponseTimestamp(
                        XmlDateTime.from_datetime(
                            datetime.datetime.now(datetime.timezone.utc)
                        )
                    ),
                    producer_ref=ParticipantRefStructure("OJP2NOVA"),
                    error_condition=ServiceDeliveryStructure.ErrorCondition(
                        other_error=OtherError(message)
                    ),
                )
            )
        )
        return self.serializer.render(ojp, ns_map=self.ns_map)
