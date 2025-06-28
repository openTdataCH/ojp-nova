from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class MatrixFaultEnum(Enum):
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_ASPECT_DISPLAYED = "incorrectAspectDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"
