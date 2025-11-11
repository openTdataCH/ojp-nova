from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AllModesEnumeration(Enum):
    """
    Union of VEHICLE and continuous MODEs.
    """

    WALK = "walk"
    CAR = "car"
    TAXI = "taxi"
    CYCLE = "cycle"
    DRT = "drt"
    MOVING_WALKWAY = "movingWalkway"
    THROUGH = "through"
