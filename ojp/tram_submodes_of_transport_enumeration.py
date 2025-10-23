from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TramSubmodesOfTransportEnumeration(Enum):
    """
    Values for Tram ModesOfTransport: TPEG pti_table_06, loc_table_12.
    """
    PTI6_0 = "pti6_0"
    LOC12_0 = "loc12_0"
    UNKNOWN = "unknown"
    PTI6_1 = "pti6_1"
    LOC12_1 = "loc12_1"
    CITY_TRAM = "cityTram"
    PTI6_2 = "pti6_2"
    LOCAL_TRAM_SERVICE = "localTramService"
    PTI6_3 = "pti6_3"
    REGIONAL_TRAM = "regionalTram"
    PTI6_4 = "pti6_4"
    LOC12_2 = "loc12_2"
    SIGHTSEEING_TRAM = "sightseeingTram"
    PTI6_5 = "pti6_5"
    SHUTTLE_TRAM = "shuttleTram"
    PTI6_6 = "pti6_6"
    ALL_TRAM_SERVICES = "allTramServices"
    PTI6_255 = "pti6_255"
    LOC12_255 = "loc12_255"
    UNDEFINED_TRAM_SERVICE = "undefinedTramService"
