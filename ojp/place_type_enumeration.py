from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PlaceTypeEnumeration(Enum):
    STOP = "stop"
    ADDRESS = "address"
    POI = "poi"
    COORD = "coord"
    TOPOGRAPHIC_PLACE = "topographicPlace"
