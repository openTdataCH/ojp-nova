from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DepartureBoardingActivityEnumeration(Enum):
    """
    Allowed types activity for Boarding.
    """
    BOARDING = "boarding"
    NO_BOARDING = "noBoarding"
    PASS_THRU = "passThru"
