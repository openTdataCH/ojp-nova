from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CoachSubmodesOfTransportEnumeration(Enum):
    """
    Values for Coach ModesOfTransport: TPEG pti_table_03.
    """
    PTI3_0 = "pti3_0"
    UNKNOWN = "unknown"
    PTI3_1 = "pti3_1"
    INTERNATIONAL_COACH_SERVICE = "internationalCoachService"
    PTI3_2 = "pti3_2"
    NATIONAL_COACH_SERVICE = "nationalCoachService"
    PTI3_3 = "pti3_3"
    SHUTTLE_COACH_SERVICE = "shuttleCoachService"
    PTI3_4 = "pti3_4"
    REGIONAL_COACH_SERVICE = "regionalCoachService"
    PTI3_5 = "pti3_5"
    SPECIAL_COACH_SERVICE = "specialCoachService"
    PTI3_6 = "pti3_6"
    SIGHTSEEING_COACH_SERVICE = "sightseeingCoachService"
    PTI3_7 = "pti3_7"
    TOURIST_COACH_SERVICE = "touristCoachService"
    PTI3_8 = "pti3_8"
    COMMUTER_COACH_SERVICE = "commuterCoachService"
    PTI3_9 = "pti3_9"
    ALL_COACH_SERVICES = "allCoachServices"
    PTI3_255 = "pti3_255"
    UNDEFINED = "undefined"
