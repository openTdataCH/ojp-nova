import datetime

from xsdata.models.datatype import XmlDateTime

from api.SerializerUtil import SerializerUtil
from api.ErrorResponseProvider import ErrorResponseProvider
from ojp2 import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError


class ErrorResponseProviderOjp2(ErrorResponseProvider):
    ns_map = SerializerUtil.ns_map
    serializer = SerializerUtil.serializer

    def provide_error_response_content(self, message: str) -> str:
        ojp = Ojp(ojpresponse=Ojpresponse(service_delivery=
                                          ServiceDelivery(response_timestamp=XmlDateTime.from_datetime(
                                              datetime.datetime.now(datetime.timezone.utc)),
                                                          producer_ref="OJP2NOVA",
                                                          error_condition=ServiceDeliveryStructure.ErrorCondition(
                                                              other_error=OtherError(message)))))
        return self.serializer.render(ojp, ns_map=self.ns_map)
