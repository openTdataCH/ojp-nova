from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class DenyReasonEnum(Enum):
    UNKNOWN_REASON = "unknownReason"
    WRONG_CATALOGUE = "wrongCatalogue"
    WRONG_FILTER = "wrongFilter"
    WRONG_ORDER = "wrongOrder"
    WRONG_PARTNER = "wrongPartner"
