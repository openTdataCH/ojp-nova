from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TurnActionEnumeration(Enum):
    """
    The range of alternative turns that can be described.
    """
    SHARP_LEFT = "sharp left"
    LEFT = "left"
    HALF_LEFT = "half left"
    STRAIGHT_ON = "straight on"
    HALF_RIGHT = "half right"
    RIGHT = "right"
    SHARP_RIGHT = "sharp right"
    UTURN = "uturn"
