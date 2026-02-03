import datetime

from xsdata.models.datatype import XmlDateTime

from api.ErrorResponseContentProvider import ErrorResponseContentProvider
from api.SerializerUtil import SerializerUtil
from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError


class ErrorResponseContentProviderOjp1(ErrorResponseContentProvider):
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
