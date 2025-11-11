from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class GuidanceAdviceEnumeration(Enum):
    """Several types of guidance advice given to traveller.

    Suitable values may differ by MODE (e.g., a car driver needs
    different advice than a person walking for a transfer.

    :cvar ORIGIN: Defining origin.
    :cvar DESTINATION: Defining a destination.
    :cvar CONTINUE: Continue on the same street/road/path.
    :cvar KEEP: Keep going on the same street/road/path.
    :cvar TURN: When this value is used, you always must consider the
        value in TurnAction as well. There must be a TurnAction present
        if "turn" is used.
    :cvar LEAVE: Can be something like an elevator or a vehicle.
    :cvar ENTER: Can be something like an elevator or a vehicle.
    :cvar ENTER_ROUNDABOUT: Entering a roundabout.
    :cvar STAY_IN_ROUNDABOUT: Staying in the roundabout.
    :cvar LEAVE_ROUNDABOUT: Leave the roundabout.
    :cvar ENTER_BUILTUP_AREA: Entering a built-up area / community.
    :cvar LEAVE_BUILTUP_AREA: Leave the built-up area / community.
    :cvar FREEWAY_ACCESS_RAMP: Access lane to highway or the like.
    :cvar UNKNOWN_LANE_CHOICE: If it is unclear which lane to choose.
    :cvar LEFT_LANE: If there are more than 2 lanes, then TurnAction
        half_left, left, sharp_left may help decide.
    :cvar MIDDLE_LANE: If there are more than 3 lanes, then Turnaction
        straight defines the middle one.
    :cvar RIGHT_LANE: If there are more than 2 lanes, then TurnAction
        half_right, right, sharp_right may help decide.
    :cvar UNKNOWN_TURNING_KIND:
    """

    ORIGIN = "origin"
    DESTINATION = "destination"
    CONTINUE = "continue"
    KEEP = "keep"
    TURN = "turn"
    LEAVE = "leave"
    ENTER = "enter"
    ENTER_ROUNDABOUT = "enter_roundabout"
    STAY_IN_ROUNDABOUT = "stay_in_roundabout"
    LEAVE_ROUNDABOUT = "leave_roundabout"
    ENTER_BUILTUP_AREA = "enter_builtup_area"
    LEAVE_BUILTUP_AREA = "leave_builtup_area"
    FREEWAY_ACCESS_RAMP = "freewayAccessRamp"
    UNKNOWN_LANE_CHOICE = "unknown_lane_choice"
    LEFT_LANE = "left_lane"
    MIDDLE_LANE = "middle_lane"
    RIGHT_LANE = "right_lane"
    UNKNOWN_TURNING_KIND = "unknown_turning_kind"
