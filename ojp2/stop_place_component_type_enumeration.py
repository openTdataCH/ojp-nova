from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class StopPlaceComponentTypeEnumeration(Enum):
    """
    Enumeration of SITE COMPONENT Types.
    """

    QUAY = "quay"
    ACCESS_SPACE = "accessSpace"
    ENTRANCE = "entrance"
    BOARDING_POSITION = "boardingPosition"
    STOPPING_PLACE = "stoppingPlace"
