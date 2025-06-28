from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ResponseEnum(Enum):
    ACKNOWLEDGE = "acknowledge"
    CATALOGUE_REQUEST_DENIED = "catalogueRequestDenied"
    FILTER_REQUEST_DENIED = "filterRequestDenied"
    REQUEST_DENIED = "requestDenied"
    SUBSCRIPTION_REQUEST_DENIED = "subscriptionRequestDenied"
