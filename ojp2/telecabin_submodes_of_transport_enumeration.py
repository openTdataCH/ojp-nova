from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TelecabinSubmodesOfTransportEnumeration(Enum):
    """Values for Telecabin ModesOfTransport: TPEG pti_table_09, pts_table_109 and loc_table_14.

    :cvar UNKNOWN: TPEG Pts109_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: Submode of transport is not supported in this list.
    :cvar TELECABIN:
    :cvar CABLE_CAR:
    :cvar LIFT:
    :cvar CHAIR_LIFT:
    :cvar DRAG_LIFT:
    :cvar TELECABIN_LINK:
    :cvar SCHEDULED: TPEG Pts109_1 (SIRI 2.1)
    :cvar UNSCHEDULED: TPEG Pts109_2 (SIRI 2.1)
    :cvar UNDEFINED_TELECABIN_SERVICE: TPEG Pts109_255 (SIRI 2.1) - see
        also 'undefined'.
    :cvar SMALL_TELECABIN:
    :cvar EGG_LIFT:
    :cvar MINERAL_BUCKETS:
    :cvar ALL_TELECABIN_SERVICES:
    :cvar PTI9_0: DEPRECATED since SIRI 2.1
    :cvar PTI9_1: DEPRECATED since SIRI 2.1
    :cvar PTI9_2: DEPRECATED since SIRI 2.1
    :cvar PTI9_3: DEPRECATED since SIRI 2.1
    :cvar PTI9_4: DEPRECATED since SIRI 2.1
    :cvar PTI9_5: DEPRECATED since SIRI 2.1
    :cvar PTI9_6: DEPRECATED since SIRI 2.1
    :cvar PTI9_7: DEPRECATED since SIRI 2.1
    :cvar PTI9_255: DEPRECATED since SIRI 2.1
    :cvar LOC14_0: DEPRECATED since SIRI 2.1
    :cvar LOC14_1: DEPRECATED since SIRI 2.1
    :cvar LOC14_3: DEPRECATED since SIRI 2.1
    :cvar LOC14_4: DEPRECATED since SIRI 2.1
    :cvar LOC14_52: DEPRECATED since SIRI 2.1
    :cvar LOC14_6: DEPRECATED since SIRI 2.1
    :cvar LOC14_7: DEPRECATED since SIRI 2.1
    :cvar LOC14_8: DEPRECATED since SIRI 2.1
    :cvar LOC14_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    TELECABIN = "telecabin"
    CABLE_CAR = "cableCar"
    LIFT = "lift"
    CHAIR_LIFT = "chairLift"
    DRAG_LIFT = "dragLift"
    TELECABIN_LINK = "telecabinLink"
    SCHEDULED = "scheduled"
    UNSCHEDULED = "unscheduled"
    UNDEFINED_TELECABIN_SERVICE = "undefinedTelecabinService"
    SMALL_TELECABIN = "smallTelecabin"
    EGG_LIFT = "eggLift"
    MINERAL_BUCKETS = "mineralBuckets"
    ALL_TELECABIN_SERVICES = "allTelecabinServices"
    PTI9_0 = "pti9_0"
    PTI9_1 = "pti9_1"
    PTI9_2 = "pti9_2"
    PTI9_3 = "pti9_3"
    PTI9_4 = "pti9_4"
    PTI9_5 = "pti9_5"
    PTI9_6 = "pti9_6"
    PTI9_7 = "pti9_7"
    PTI9_255 = "pti9_255"
    LOC14_0 = "loc14_0"
    LOC14_1 = "loc14_1"
    LOC14_3 = "loc14_3"
    LOC14_4 = "loc14_4"
    LOC14_52 = "loc14_52"
    LOC14_6 = "loc14_6"
    LOC14_7 = "loc14_7"
    LOC14_8 = "loc14_8"
    LOC14_255 = "loc14_255"
