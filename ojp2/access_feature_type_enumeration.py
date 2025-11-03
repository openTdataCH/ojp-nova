from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AccessFeatureTypeEnumeration(Enum):
    """
    Allowed values for a AccessFeature.
    """

    ELEVATOR = "elevator"
    STAIRS = "stairs"
    SERIES_OF_STAIRS = "seriesOfStairs"
    SINGLE_STEP = "singleStep"
    SERIES_OF_SINGLE_STEPS = "seriesOfSingleSteps"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    FOOTPATH = "footpath"
    SHUTTLE = "shuttle"
    OTHER = "other"
    UNKNOWN = "unknown"
