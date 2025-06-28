from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PersonalModesEnumeration(Enum):
    """TYPE OF MODE that can be used in an individual context.

    PERSONAL MODE in TM 6.2.

    :cvar FOOT:
    :cvar BICYCLE:
    :cvar CAR:
    :cvar MOTORCYCLE:
    :cvar TRUCK:
    :cvar SCOOTER:
    :cvar OTHER: Only to be used when no other type applies.
    """

    FOOT = "foot"
    BICYCLE = "bicycle"
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"
    SCOOTER = "scooter"
    OTHER = "other"
