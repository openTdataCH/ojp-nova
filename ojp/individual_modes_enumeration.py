from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class IndividualModesEnumeration(Enum):
    """
    modes which an individual powers themselves (such as walk, cycle)
    """
    WALK = "walk"
    CYCLE = "cycle"
    TAXI = "taxi"
    SELF_DRIVE_CAR = "self-drive-car"
    OTHERS_DRIVE_CAR = "others-drive-car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"
