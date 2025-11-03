from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TripRefineParamStructureCyclingProfile(Enum):
    """
    :cvar FAST: Fastest cycle route
    :cvar GREEN: Greenest cycle route
    :cvar COMFORTABLE: Family friendly and leisurely route
    """

    FAST = "fast"
    GREEN = "green"
    COMFORTABLE = "comfortable"
