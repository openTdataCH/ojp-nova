from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FareClassFacilityEnumeration(Enum):
    """Values for FareClass Facility: TPEG pti_table 23."""

    UNKNOWN = "unknown"
    PTI23_0 = "pti23_0"
    PTI23_6 = "pti23_6"
    FIRST_CLASS = "firstClass"
    PTI23_7 = "pti23_7"
    SECOND_CLASS = "secondClass"
    PTI23_8 = "pti23_8"
    THIRD_CLASS = "thirdClass"
    PTI23_9 = "pti23_9"
    ECONOMY_CLASS = "economyClass"
    PTI23_10 = "pti23_10"
    BUSINESS_CLASS = "businessClass"
