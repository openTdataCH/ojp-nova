from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class StopEventTypeEnumeration(Enum):
    """
    Departure or arrival events or both.
    """

    DEPARTURE = "departure"
    ARRIVAL = "arrival"
    BOTH = "both"
