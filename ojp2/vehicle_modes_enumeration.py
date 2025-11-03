from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleModesEnumeration(Enum):
    """
    MODEs of transport applicable to timetabled public transport.
    """

    AIR = "air"
    BUS = "bus"
    COACH = "coach"
    FERRY = "ferry"
    METRO = "metro"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND = "underground"
