from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class UpdateMethodEnum(Enum):
    ALL_ELEMENT_UPDATE = "allElementUpdate"
    SINGLE_ELEMENT_UPDATE = "singleElementUpdate"
    SNAPSHOT = "snapshot"
