from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TransitionEnumeration(Enum):
    """
    Transition types for interchanges.
    """

    UP = "up"
    DOWN = "down"
    LEVEL = "level"
    UP_AND_DOWN = "upAndDown"
    DOWN_AND_UP = "downAndUp"
