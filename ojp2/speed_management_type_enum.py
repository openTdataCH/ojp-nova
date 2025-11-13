from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class SpeedManagementTypeEnum(Enum):
    ACTIVE_SPEED_CONTROL_IN_OPERATION = "activeSpeedControlInOperation"
    DO_NOT_SLOWDOWN_UNNECESSARILY = "doNotSlowdownUnnecessarily"
    OBSERVE_SPEED_LIMIT = "observeSpeedLimit"
    POLICE_SPEED_CHECKS_IN_OPERATION = "policeSpeedChecksInOperation"
    REDUCE_YOUR_SPEED = "reduceYourSpeed"
    OTHER = "other"
