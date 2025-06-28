from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class DelaysTypeEnum(Enum):
    DELAYS = "delays"
    DELAYS_OF_UNCERTAIN_DURATION = "delaysOfUncertainDuration"
    LONG_DELAYS = "longDelays"
    VERY_LONG_DELAYS = "veryLongDelays"
