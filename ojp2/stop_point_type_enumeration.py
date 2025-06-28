from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class StopPointTypeEnumeration(Enum):
    """Values for TPEG Pts017 - ServiceDeliveryPointType

    :cvar UNKNOWN: TPEG Pts17_0, unknown
    :cvar PLATFORM_NUMBER: TPEG Pts17_1, platform number
    :cvar TERMINAL_GATE: TPEG Pts17_2, terminal gate
    :cvar FERRY_BERTH: TPEG Pts17_3, ferry berth
    :cvar HARBOUR_PIER: TPEG Pts17_4, harbour pier
    :cvar LANDING_STAGE: TPEG Pts17_5, unknown
    :cvar BUS_STOP: TPEG Pts17_6, bus stop
    :cvar UNDEFINED_STOP_POINT_TYPE: TPEG Pts17_255, undefined service
        delivery point type
    :cvar UNDEFINED_BOOKING_INFORMATION: DEPRECATED since SIRI 2.1 - use
        undefinedStopPointType
    """

    UNKNOWN = "unknown"
    PLATFORM_NUMBER = "platformNumber"
    TERMINAL_GATE = "terminalGate"
    FERRY_BERTH = "ferryBerth"
    HARBOUR_PIER = "harbourPier"
    LANDING_STAGE = "landingStage"
    BUS_STOP = "busStop"
    UNDEFINED_STOP_POINT_TYPE = "undefinedStopPointType"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
