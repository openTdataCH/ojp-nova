from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class EquipmentOrSystemFaultTypeEnum(Enum):
    NOT_WORKING = "notWorking"
    OUT_OF_SERVICE = "outOfService"
    WORKING_INCORRECTLY = "workingIncorrectly"
    WORKING_INTERMITTENTLY = "workingIntermittently"
