from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PlaceTypeEnumeration(Enum):
    """
    :cvar STOP: stop covers StopPlace and StopPoint. The main reason is
        that many systems may only return either STOP PLACE/QUAY
        information or SCHEDULED STOP POINTs.
    :cvar ADDRESS:
    :cvar POI:
    :cvar COORD: Deprecated. Use location instead.
    :cvar LOCATION: Geographic position consisting of coordinates.
        Replaces the deprecated value coord.
    :cvar TOPOGRAPHIC_PLACE:
    """

    STOP = "stop"
    ADDRESS = "address"
    POI = "poi"
    COORD = "coord"
    LOCATION = "location"
    TOPOGRAPHIC_PLACE = "topographicPlace"
