from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AccessFeatureTypeEnumeration(Enum):
    """
    Allowed values for a AccessFeature.
    """
    LIFT = "lift"
    STAIRS = "stairs"
    SERIES_OF_STAIRS = "seriesOfStairs"
    ESCALATOR = "escalator"
    RAMP = "ramp"
    FOOTPATH = "footpath"
