from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MetroSubmodesOfTransportEnumeration(Enum):
    """Values for Metro ModesOfTransport: TPEG pti_table_04 and pts_table_104.

    :cvar UNKNOWN: TPEG Pts104_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: Submode of transport is not supported in this list.
    :cvar METRO:
    :cvar TUBE:
    :cvar URBAN_RAILWAY:
    :cvar ALL_RAIL_SERVICES:
    :cvar METRO_SERVICE: TPEG Pts104_1 (SIRI 2.1) - see also 'metro'.
    :cvar NIGHT_METRO_SERVICE: TPEG Pts104_2 (SIRI 2.1)
    :cvar EXPRESS_METRO_SERVICE: TPEG Pts104_3 (SIRI 2.1)
    :cvar UNDEFINED_URBAN_RAILWAY_SERVICE: TPEG Pts104_255 (SIRI 2.1) -
        see also 'undefined'.
    :cvar PTI4_0: DEPRECATED since SIRI 2.1
    :cvar PTI4_1: DEPRECATED since SIRI 2.1
    :cvar PTI4_2: DEPRECATED since SIRI 2.1
    :cvar PTI4_3: DEPRECATED since SIRI 2.1
    :cvar PTI4_4: DEPRECATED since SIRI 2.1
    :cvar PTI4_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"
    ALL_RAIL_SERVICES = "allRailServices"
    METRO_SERVICE = "metroService"
    NIGHT_METRO_SERVICE = "nightMetroService"
    EXPRESS_METRO_SERVICE = "expressMetroService"
    UNDEFINED_URBAN_RAILWAY_SERVICE = "undefinedUrbanRailwayService"
    PTI4_0 = "pti4_0"
    PTI4_1 = "pti4_1"
    PTI4_2 = "pti4_2"
    PTI4_3 = "pti4_3"
    PTI4_4 = "pti4_4"
    PTI4_255 = "pti4_255"
