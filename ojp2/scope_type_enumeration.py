from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ScopeTypeEnumeration(Enum):
    """Values for ScopeType - TPEG Pts36, AlertForType with additional values

    :cvar UNKNOWN: TPEG Pts36_0, unknown
    :cvar STOP_PLACE: TPEG Pts36_1, STOP PLACE
    :cvar LINE: TPEG Pts36_2, line
    :cvar ROUTE: TPEG Pts36_3, route
    :cvar PUBLIC_TRANSPORT_SERVICE: TPEG Pts36_4, individual PT service
    :cvar OPERATOR: TPEG Pts36_5, operator
    :cvar CITY: TPEG Pts36_6, city
    :cvar AREA: TPEG Pts36_7, area
    :cvar STOP_POINT: TPEG Pts36_8, stop point
    :cvar STOP_PLACE_COMPONENT: STOP PLACE component
    :cvar PLACE: place
    :cvar NETWORK: network
    :cvar VEHICLE_JOURNEY: vehicle journey
    :cvar DATED_VEHICLE_JOURNEY: dated vehicle journey
    :cvar CONNECTION_LINK: connection link
    :cvar INTERCHANGE: interchange
    :cvar ALL_PT: TPEG Pts36_0, unknown
    :cvar GENERAL: general
    :cvar ROAD: road
    :cvar UNDEFINED: TPEG Pts36_255, undefined
    """

    UNKNOWN = "unknown"
    STOP_PLACE = "stopPlace"
    LINE = "line"
    ROUTE = "route"
    PUBLIC_TRANSPORT_SERVICE = "publicTransportService"
    OPERATOR = "operator"
    CITY = "city"
    AREA = "area"
    STOP_POINT = "stopPoint"
    STOP_PLACE_COMPONENT = "stopPlaceComponent"
    PLACE = "place"
    NETWORK = "network"
    VEHICLE_JOURNEY = "vehicleJourney"
    DATED_VEHICLE_JOURNEY = "datedVehicleJourney"
    CONNECTION_LINK = "connectionLink"
    INTERCHANGE = "interchange"
    ALL_PT = "allPT"
    GENERAL = "general"
    ROAD = "road"
    UNDEFINED = "undefined"
