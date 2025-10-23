from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class StopPointTypeEnumeration(Enum):
    """
    Values for TBookingStatus TPEG pti_table17.
    """
    PTI17_0 = "pti17_0"
    UNKNOWN = "unknown"
    PTI17_1 = "pti17_1"
    PLATFORM_NUMBER = "platformNumber"
    PTI17_2 = "pti17_2"
    TERMINAL_GATE = "terminalGate"
    PTI17_3 = "pti17_3"
    FERRY_BERTH = "ferryBerth"
    PTI17_4 = "pti17_4"
    HARBOUR_PIER = "harbourPier"
    PTI17_5 = "pti17_5"
    LANDING_STAGE = "landingStage"
    PTI17_6 = "pti17_6"
    BUS_STOP = "busStop"
    PTI17_255 = "pti17_255"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
