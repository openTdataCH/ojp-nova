from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class ContinuousModesEnumeration(Enum):
    """
    Types of cmodes that  run at any time without a timetable.
    """
    WALK = "walk"
    DEMAND_RESPONSIVE = "demandResponsive"
    REPLACEMENT_SERVICE = "replacementService"
