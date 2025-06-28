from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AccessibilityFeatureEnumeration2(Enum):
    """Values for AccessibilityFeature - TPEG Pts040 and IFOPT

    :cvar UNKNOWN: IFOPT, TPEG Pts40_0, unknown
    :cvar SINGLE_STEP: TPEG Pts40_1, single step
    :cvar STAIRS: IFOPT, TPEG Pts40_2, stairs
    :cvar ESCALATOR: IFOPT, TPEG Pts40_3, escalator
    :cvar TRAVELATOR: IFOPT, TPEG Pts40_4, travelator / moving walkway
    :cvar LIFT: IFOPT, TPEG Pts40_5, lift / elevator
    :cvar RAMP: IFOPT, TPEG Pts40_6, ramp
    :cvar MIND_THE_GAP: TPEG Pts40_7, mind the gap
    :cvar TACTILE_PAVING: TPEG Pts40_8, tactile paving
    :cvar SERIES_OF_STAIRS: IFOPT, series of stairs
    :cvar SHUTTLE: IFOPT, shuttle
    :cvar BARRIER: IFOPT, barrier
    :cvar NARROW_ENTRANCE: IFOPT, narrow entrance
    :cvar CONFINED_SPACE: IFOPT, confined space
    :cvar QUEUE_MANAGEMENT: IFOPT, queue management
    :cvar NONE: IFOPT, none
    :cvar OTHER: IFOPT, other
    :cvar UNDEFINED: TPEG Pts40_255, undefined accessibility feature
        type
    """

    UNKNOWN = "unknown"
    SINGLE_STEP = "singleStep"
    STAIRS = "stairs"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    LIFT = "lift"
    RAMP = "ramp"
    MIND_THE_GAP = "mindTheGap"
    TACTILE_PAVING = "tactilePaving"
    SERIES_OF_STAIRS = "seriesOfStairs"
    SHUTTLE = "shuttle"
    BARRIER = "barrier"
    NARROW_ENTRANCE = "narrowEntrance"
    CONFINED_SPACE = "confinedSpace"
    QUEUE_MANAGEMENT = "queueManagement"
    NONE = "none"
    OTHER = "other"
    UNDEFINED = "undefined"
