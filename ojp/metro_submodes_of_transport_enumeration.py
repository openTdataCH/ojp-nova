from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MetroSubmodesOfTransportEnumeration(Enum):
    """
    Values for Metro ModesOfTransport: TPEG pti_table_04.
    """
    PTI4_0 = "pti4_0"
    UNKNOWN = "unknown"
    PTI4_1 = "pti4_1"
    METRO = "metro"
    PTI4_2 = "pti4_2"
    TUBE = "tube"
    PTI4_3 = "pti4_3"
    URBAN_RAILWAY = "urbanRailway"
    PTI4_4 = "pti4_4"
    ALL_RAIL_SERVICES = "allRailServices"
    PTI4_255 = "pti4_255"
    UNDEFINED = "undefined"
