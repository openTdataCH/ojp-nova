from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class AccessModesEnumeration(Enum):
    """
    Allowed categroies of access to stop place.
    """
    FOOT = "foot"
    BICYCLE = "bicycle"
    CAR = "car"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
