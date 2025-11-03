from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DeliveryMethodEnumeration(Enum):
    """Delivery Method: Fetched or Direct Delivery."""

    DIRECT = "direct"
    FETCHED = "fetched"
