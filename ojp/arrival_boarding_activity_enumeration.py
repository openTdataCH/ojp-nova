from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ArrivalBoardingActivityEnumeration(Enum):
    """
    Allowed types activity for Alighting.
    """
    ALIGHTING = "alighting"
    NO_ALIGHTING = "noAlighting"
    PASS_THRU = "passThru"
