from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TurnActionEnumeration(Enum):
    """
    The range of possible turns that can be described.

    :cvar STRAIGHT_ON: 338-21 degrees
    :cvar HALF_RIGHT: 22-67 degrees
    :cvar RIGHT: 68-111 degrees
    :cvar SHARP_RIGHT: 112-157 degrees
    :cvar UTURN: 158-201 degrees
    :cvar SHARP_LEFT: 202-247 degrees
    :cvar LEFT: 248-291 degrees
    :cvar HALF_LEFT: 292-337 degrees
    :cvar UP: Upwards, the target level is in the PathLink structure.
    :cvar DOWN: Downwards, the target level is in the PathLink
        structure.
    :cvar UNKNOWN_TURN_ACTION:
    """

    STRAIGHT_ON = "straight_on"
    HALF_RIGHT = "half_right"
    RIGHT = "right"
    SHARP_RIGHT = "sharp_right"
    UTURN = "uturn"
    SHARP_LEFT = "sharp_left"
    LEFT = "left"
    HALF_LEFT = "half_left"
    UP = "up"
    DOWN = "down"
    UNKNOWN_TURN_ACTION = "unknown_turn_action"
