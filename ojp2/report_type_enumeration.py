from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ReportTypeEnumeration(Enum):
    """Values for TPEG Pti27 - ReportType

    :cvar UNKNOWN: TPEG Pti27_0, unknown
    :cvar INCIDENT: TPEG Pti27_1, incident
    :cvar GENERAL: TPEG Pti27_1_1, general
    :cvar OPERATOR: TPEG Pti27_1_2, operator
    :cvar NETWORK: TPEG Pti27_1_3, network
    :cvar STATION_TERMINAL: TPEG Pti27_2, station terminal
    :cvar STOP_POINT: TPEG Pti27_2_1, stoppoint
    :cvar CONNECTION_LINK: TPEG Pti27_2_2, connection link
    :cvar POINT: TPEG Pti27_2_3, point
    :cvar ROUTE: TPEG Pti27_3, route
    :cvar INDIVIDUAL_SERVICE: TPEG Pti27_4, individual service
    :cvar UNDEFINED: TPEG Pti27_255, undefined type
    """

    UNKNOWN = "unknown"
    INCIDENT = "incident"
    GENERAL = "general"
    OPERATOR = "operator"
    NETWORK = "network"
    STATION_TERMINAL = "stationTerminal"
    STOP_POINT = "stopPoint"
    CONNECTION_LINK = "connectionLink"
    POINT = "point"
    ROUTE = "route"
    INDIVIDUAL_SERVICE = "individualService"
    UNDEFINED = "undefined"
