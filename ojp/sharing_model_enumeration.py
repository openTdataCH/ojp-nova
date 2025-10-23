from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class SharingModelEnumeration(Enum):
    """
    Sharing service loan and return scheme.
    """
    SINGLE_STATION_BASED = "singleStationBased"
    MULTIPLE_STATION_BASED = "multipleStationBased"
    NON_STATION_BASED = "nonStationBased"
