from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CountingTypeEnumeration(Enum):
    """
    Allowed values for TypeOfCounting.
    """
    AVAILABILITY_COUNT = "availabilityCount"
    RESERVED_COUNT = "reservedCount"
    IN_USE_COUNT = "inUseCount"
    OUT_OF_ORDER_COUNT = "outOfOrderCount"
    PRESENT_COUNT = "presentCount"
    CHARGING_LEVEL = "chargingLevel"
    AVAILABLE_RUNNING_DISTANCE = "availableRunningDistance"
    CURRENT_STATE_COUNT = "currentStateCount"
