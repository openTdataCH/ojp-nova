from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class StopPlaceTypeEnumeration(Enum):
    """Values for STOP PLACE types - TPEG Pts041 and IFOPT

    :cvar UNKNOWN: TPEG Pts41_0, unknown
    :cvar RAILWAY_STATION: TPEG Pts41_1, railway station
    :cvar UNDERGROUND_STATION: TPEG Pts41_2, underground station
    :cvar TRAM_STATION: IFOPT, TPEG Pts41_3, tram station
    :cvar BUS_STATION: IFOPT, TPEG Pts41_4, bus station
    :cvar AIRPORT: IFOPT, TPEG Pts41_5, airport
    :cvar PIER: TPEG Pts41_6, pier
    :cvar HARBOUR_PORT: IFOPT, TPEG Pts41_7, harbour port
    :cvar FERRY_STOP: ,IFOPT, TPEG Pts41_8, ferry stop
    :cvar LIGHT_RAILWAY_STATION: TPEG Pts41_9, light railway station
    :cvar COGWHEEL_STATION: TPEG Pts41_10, cogwheel station
    :cvar FUNICULAR_STATION: TPEG Pts41_11, funicular station
    :cvar ROPEWAY_STATION: TPEG Pts41_12, ropeway station
    :cvar COACH_STATION: IFOPT, coach station
    :cvar FERRY_PORT: IFOPT, ferry port
    :cvar ON_STREET_BUS: IFOPT, on-street bus stop
    :cvar ON_STREET_TRAM: IFOPT, on-street tram stop
    :cvar SKI_LIFT: IFOPT, ski lift
    :cvar OTHER: IFOPT, other
    :cvar UNDEFINED_STOP_PLACE_TYPE: TPEG Pts41_255, undefined STOP
        PLACE type
    :cvar RAIL_STATION: IFOPT, deprecated (SIRI 2.1), use railwayStation
    :cvar METRO_STATION: IFOPT, deprecated (SIRI 2.1), use
        undergroundStation
    """

    UNKNOWN = "unknown"
    RAILWAY_STATION = "railwayStation"
    UNDERGROUND_STATION = "undergroundStation"
    TRAM_STATION = "tramStation"
    BUS_STATION = "busStation"
    AIRPORT = "airport"
    PIER = "pier"
    HARBOUR_PORT = "harbourPort"
    FERRY_STOP = "ferryStop"
    LIGHT_RAILWAY_STATION = "lightRailwayStation"
    COGWHEEL_STATION = "cogwheelStation"
    FUNICULAR_STATION = "funicularStation"
    ROPEWAY_STATION = "ropewayStation"
    COACH_STATION = "coachStation"
    FERRY_PORT = "ferryPort"
    ON_STREET_BUS = "onStreetBus"
    ON_STREET_TRAM = "onStreetTram"
    SKI_LIFT = "skiLift"
    OTHER = "other"
    UNDEFINED_STOP_PLACE_TYPE = "undefinedStopPlaceType"
    RAIL_STATION = "railStation"
    METRO_STATION = "metroStation"
