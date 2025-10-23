from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TrafficTypeEnum(Enum):
    ACCESS_ONLY_TRAFFIC = "accessOnlyTraffic"
    DESTINED_FOR_AIRPORT = "destinedForAirport"
    DESTINED_FOR_AIRPORT_ARRIVALS = "destinedForAirportArrivals"
    DESTINED_FOR_AIRPORT_DEPARTURES = "destinedForAirportDepartures"
    DESTINED_FOR_FERRY_SERVICE = "destinedForFerryService"
    DESTINED_FOR_RAIL_SERVICE = "destinedForRailService"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    LOCAL_TRAFFIC = "localTraffic"
    LONG_DISTANCE_TRAFFIC = "longDistanceTraffic"
    REGIONAL_TRAFFIC = "regionalTraffic"
    RESIDENTS_ONLY_TRAFFIC = "residentsOnlyTraffic"
    THROUGH_TRAFFIC = "throughTraffic"
    VISITOR_TRAFFIC = "visitorTraffic"
