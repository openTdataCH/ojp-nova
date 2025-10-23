from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class VehicleStatusEnum(Enum):
    ABANDONED = "abandoned"
    BROKEN_DOWN = "brokenDown"
    BURNT_OUT = "burntOut"
    DAMAGED = "damaged"
    DAMAGED_AND_IMMOBILIZED = "damagedAndImmobilized"
    ON_FIRE = "onFire"
