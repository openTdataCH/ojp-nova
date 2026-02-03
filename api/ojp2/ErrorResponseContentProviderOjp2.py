import datetime

from xsdata.models.datatype import XmlDateTime

from api.ErrorResponseContentProvider import ErrorResponseContentProvider
from api.SerializerUtil import SerializerUtil
from ojp2 import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError, ParticipantRefStructure, \
    ResponseTimestamp


class ErrorResponseContentProviderOjp2(ErrorResponseContentProvider):
    ns_map = SerializerUtil.ns_map
    serializer = SerializerUtil.serializer

    def provide_error_response_content(self, message: str) -> str:
        """
        Provides the ojp2 error response content for the given error message.
        """
        ojp = Ojp(ojpresponse=Ojpresponse(service_delivery=
                                          ServiceDelivery(
                                              response_timestamp=ResponseTimestamp(XmlDateTime.from_datetime(
                                              datetime.datetime.now(datetime.timezone.utc))),
                                              producer_ref=ParticipantRefStructure("OJP2NOVA"),
                                              error_condition=ServiceDeliveryStructure.ErrorCondition(
                                                              other_error=OtherError(message)))))
        return self.serializer.render(ojp, ns_map=self.ns_map)