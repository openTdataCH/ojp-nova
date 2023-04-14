from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class StopPlaceTypeEnumeration(Enum):
    """
    Enumeration of STOP PLACE types.
    """
    AIRPORT = "airport"
    RAIL_STATION = "railStation"
    METRO_STATION = "metroStation"
    COACH_STATION = "coachStation"
    BUS_STATION = "busStation"
    HARBOUR_PORT = "harbourPort"
    FERRYT_PORT = "ferrytPort"
    FERRY_STOP = "ferryStop"
    ON_STREET_BUS = "onStreetBus"
    ON_STREET_TRAM = "onStreetTram"
    SKI_LIFT = "skiLift"
    OTHER = "other"
