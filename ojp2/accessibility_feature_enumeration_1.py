from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class AccessibilityFeatureEnumeration1(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    LIFT = "lift"
    STAIRS = "stairs"
    SERIES_OF_STAIRS = "seriesOfStairs"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    SHUTTLE = "shuttle"
    BARRIER = "barrier"
    NARROW_ENTRANCE = "narrowEntrance"
    CONFINED_SPACE = "confinedSpace"
    QUEUE_MANAGEMENT = "queueManagement"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
