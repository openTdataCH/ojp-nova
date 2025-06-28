from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class AccessModesEnumeration(Enum):
    """
    Allowed categroies of access to STOP PLACE.
    """

    FOOT = "foot"
    BICYCLE = "bicycle"
    CAR = "car"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
