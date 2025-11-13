from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AccessFeatureStatusEnumeration(Enum):
    """
    Allowed values for status of the access feature.

    :cvar UNKNOWN:
    :cvar AVAILABLE:
    :cvar PARTIALLY_AVAILABLE: If partiallyAvailable is used, then some
        note should be provided in one of the descriptive elements of
        the containing PathLink
    :cvar NOT_AVAILABLE:
    """

    UNKNOWN = "unknown"
    AVAILABLE = "available"
    PARTIALLY_AVAILABLE = "partiallyAvailable"
    NOT_AVAILABLE = "notAvailable"
