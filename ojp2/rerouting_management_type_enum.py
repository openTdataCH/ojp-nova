from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ReroutingManagementTypeEnum(Enum):
    DO_NOT_FOLLOW_DIVERSION_SIGNS = "doNotFollowDiversionSigns"
    DO_NOT_USE_ENTRY = "doNotUseEntry"
    DO_NOT_USE_EXIT = "doNotUseExit"
    DO_NOT_USE_INTERSECTION_OR_JUNCTION = "doNotUseIntersectionOrJunction"
    FOLLOW_DIVERSION_SIGNS = "followDiversionSigns"
    FOLLOW_LOCAL_DIVERSION = "followLocalDiversion"
    FOLLOW_SPECIAL_MARKERS = "followSpecialMarkers"
    USE_ENTRY = "useEntry"
    USE_EXIT = "useExit"
    USE_INTERSECTION_OR_JUNCTION = "useIntersectionOrJunction"
