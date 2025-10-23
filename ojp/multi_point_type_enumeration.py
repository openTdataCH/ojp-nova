from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class MultiPointTypeEnumeration(Enum):
    """
    How the multiple origin/destination points should be considered.
    """
    ANY_POINT = "anyPoint"
    EACH_ORIGIN = "eachOrigin"
    EACH_DESTINATION = "eachDestination"
