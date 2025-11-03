from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RequestTypeEnum(Enum):
    CATALOGUE = "catalogue"
    FILTER = "filter"
    REQUEST_DATA = "requestData"
    REQUEST_HISTORICAL_DATA = "requestHistoricalData"
    SUBSCRIPTION = "subscription"
