from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FacilityStatusEnumeration(Enum):
    """
    Allowed values for the status of a MONITORED FACILITY.
    """
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    PARTIALLY_AVAILABLE = "partiallyAvailable"
    ADDED = "added"
    REMOVED = "removed"
