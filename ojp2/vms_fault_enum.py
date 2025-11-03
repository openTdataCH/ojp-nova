from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class VmsFaultEnum(Enum):
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_MESSAGE_DISPLAYED = "incorrectMessageDisplayed"
    INCORRECT_PICTOGRAM_DISPLAYED = "incorrectPictogramDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"
