from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ReportTypeEnumeration(Enum):
    """
    Values for Report Type TPEG pti_table 27.
    """
    VALUE_27_0 = "27_0"
    UNKNOWN = "unknown"
    VALUE_27_1 = "27_1"
    INCIDENT = "incident"
    VALUE_27_1_ALIAS_1 = "27_1_Alias_1"
    GENERAL = "general"
    VALUE_2_27_1_ALIAS_2 = "2_27_1_Alias_2"
    OPERATOR = "operator"
    VALUE_2_27_1_ALIAS_3 = "2_27_1_Alias_3"
    NETWORK = "network"
    VALUE_27_3 = "27_3"
    ROUTE = "route"
    VALUE_27_2 = "27_2"
    STATION_TERMINAL = "stationTerminal"
    VALUE_27_2_ALIAS_1 = "27_2_Alias_1"
    STOP_POINT = "stopPoint"
    VALUE_27_2_ALIAS_2 = "27_2_Alias_2"
    CONNECTION_LINK = "connectionLink"
    VALUE_27_2_ALIAS_3 = "27_2_Alias_3"
    POINT = "point"
    VALUE_27_4 = "27_4"
    INDIVIDUAL_SERVICE = "individualService"
    VALUE_27_255 = "27_255"
    UNDEFINED = "undefined"
