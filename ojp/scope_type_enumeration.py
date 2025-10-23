from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ScopeTypeEnumeration(Enum):
    """
    Values for ScopeType.
    """
    GENERAL = "general"
    OPERATOR = "operator"
    NETWORK = "network"
    ROUTE = "route"
    LINE = "line"
    PLACE = "place"
    STOP_PLACE = "stopPlace"
    STOP_PLACE_COMPONENT = "stopPlaceComponent"
    STOP_POINT = "stopPoint"
    VEHICLE_JOURNEY = "vehicleJourney"
    DATED_VEHICLE_JOURNEY = "datedVehicleJourney"
    CONNECTION_LINK = "connectionLink"
    INTERCHANGE = "interchange"
    ALL_PT = "allPT"
    ROAD = "road"
