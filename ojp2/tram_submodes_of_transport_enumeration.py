from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TramSubmodesOfTransportEnumeration(Enum):
    """Values for Tram ModesOfTransport: TPEG pti_table_06, pts_table_104 and loc_table_12.

    :cvar UNKNOWN: TPEG Pts104_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: (SIRI 2.1) - see also 'undefinedTramService'.
    :cvar CITY_TRAM:
    :cvar LOCAL_TRAM: (SIRI 2.1) - see also 'localTramService'.
    :cvar REGIONAL_TRAM:
    :cvar SIGHTSEEING_TRAM:
    :cvar SHUTTLE_TRAM:
    :cvar TRAIN_TRAM: (SIRI 2.1)
    :cvar TRAM_SERVICE: TPEG Pts104_4 (SIRI 2.1)
    :cvar CITY_TRAM_SERVICE: TPEG Pts104_5 (SIRI 2.1) - see also
        'cityTram'.
    :cvar REGIONAL_TRAM_SERVICE: TPEG Pts104_6 (SIRI 2.1) - see also
        'regionalTram'.
    :cvar SIGHTSEEING_TRAM_SERVICE: TPEG Pts104_7 (SIRI 2.1) - see also
        'sightseeingTram'.
    :cvar NIGHT_TRAM_SERVICE: TPEG Pts104_8 (SIRI 2.1)
    :cvar SHUTTLE_TRAM_SERVICE: TPEG Pts104_9 (SIRI 2.1) - see also
        'shuttleTram'.
    :cvar UNDEFINED_URBAN_RAILWAY_SERVICE: TPEG Pts104_255 (SIRI 2.1) -
        see also 'undefined'.
    :cvar LOCAL_TRAM_SERVICE:
    :cvar UNDEFINED_TRAM_SERVICE: Submode of transport is not supported
        in this list.
    :cvar ALL_TRAM_SERVICES:
    :cvar PTI6_0: DEPRECATED since SIRI 2.1
    :cvar PTI6_1: DEPRECATED since SIRI 2.1
    :cvar PTI6_2: DEPRECATED since SIRI 2.1
    :cvar PTI6_3: DEPRECATED since SIRI 2.1
    :cvar PTI6_4: DEPRECATED since SIRI 2.1
    :cvar PTI6_5: DEPRECATED since SIRI 2.1
    :cvar PTI6_6: DEPRECATED since SIRI 2.1
    :cvar PTI6_255: DEPRECATED since SIRI 2.1
    :cvar LOC12_0: DEPRECATED since SIRI 2.1
    :cvar LOC12_1: DEPRECATED since SIRI 2.1
    :cvar LOC12_2: DEPRECATED since SIRI 2.1
    :cvar LOC12_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    CITY_TRAM = "cityTram"
    LOCAL_TRAM = "localTram"
    REGIONAL_TRAM = "regionalTram"
    SIGHTSEEING_TRAM = "sightseeingTram"
    SHUTTLE_TRAM = "shuttleTram"
    TRAIN_TRAM = "trainTram"
    TRAM_SERVICE = "tramService"
    CITY_TRAM_SERVICE = "cityTramService"
    REGIONAL_TRAM_SERVICE = "regionalTramService"
    SIGHTSEEING_TRAM_SERVICE = "sightseeingTramService"
    NIGHT_TRAM_SERVICE = "nightTramService"
    SHUTTLE_TRAM_SERVICE = "shuttleTramService"
    UNDEFINED_URBAN_RAILWAY_SERVICE = "undefinedUrbanRailwayService"
    LOCAL_TRAM_SERVICE = "localTramService"
    UNDEFINED_TRAM_SERVICE = "undefinedTramService"
    ALL_TRAM_SERVICES = "allTramServices"
    PTI6_0 = "pti6_0"
    PTI6_1 = "pti6_1"
    PTI6_2 = "pti6_2"
    PTI6_3 = "pti6_3"
    PTI6_4 = "pti6_4"
    PTI6_5 = "pti6_5"
    PTI6_6 = "pti6_6"
    PTI6_255 = "pti6_255"
    LOC12_0 = "loc12_0"
    LOC12_1 = "loc12_1"
    LOC12_2 = "loc12_2"
    LOC12_255 = "loc12_255"
