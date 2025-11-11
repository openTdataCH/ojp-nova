from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CoachSubmodesOfTransportEnumeration(Enum):
    """Values for Coach ModesOfTransport: TPEG pti_table_03 and pts_table_103.

    :cvar UNKNOWN: TPEG Pts103_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: Submode of transport is not supported in this list.
    :cvar INTERNATIONAL_COACH: (SIRI 2.1) - see also
        'internationalCoachService'.
    :cvar NATIONAL_COACH: (SIRI 2.1) - see also 'nationalCoachService'.
    :cvar SHUTTLE_COACH: (SIRI 2.1) - see also 'shuttleCoachService'.
    :cvar REGIONAL_COACH: (SIRI 2.1) - see also 'regionalCoachService'.
    :cvar SPECIAL_COACH: (SIRI 2.1) - see also 'specialCoachService'.
    :cvar SCHOOL_COACH: (SIRI 2.1)
    :cvar SIGHTSEEING_COACH: (SIRI 2.1) - see also
        'sightseeingCoachService'.
    :cvar TOURIST_COACH: (SIRI 2.1) - see also 'touristCoachService'.
    :cvar COMMUTER_COACH: (SIRI 2.1) - see also 'commuterCoachService'.
    :cvar INTERNATIONAL_COACH_SERVICE: TPEG Pts103_1
    :cvar NATIONAL_COACH_SERVICE: TPEG Pts103_2
    :cvar SHUTTLE_COACH_SERVICE: TPEG Pts103_3
    :cvar REGIONAL_COACH_SERVICE: TPEG Pts103_4
    :cvar ADDITIONAL_COACH_SERVICE: TPEG Pts103_5 (SIRI 2.1)
    :cvar NIGHT_COACH_SERVICE: TPEG Pts103_6 (SIRI 2.1)
    :cvar SPECIAL_COACH_SERVICE: TPEG Pts103_7
    :cvar SIGHTSEEING_COACH_SERVICE: TPEG Pts103_8
    :cvar TOURIST_COACH_SERVICE: TPEG Pts103_9
    :cvar COMMUTER_COACH_SERVICE: TPEG Pts103_10
    :cvar ON_DEMAND_SERVICE: TPEG Pts103_11 (SIRI 2.1)
    :cvar UNDEFINED_COACH_SERVICE: TPEG Pts103_255 (SIRI 2.1) - see also
        'undefined'.
    :cvar ALL_COACH_SERVICES:
    :cvar PTI3_0: DEPRECATED since SIRI 2.1
    :cvar PTI3_1: DEPRECATED since SIRI 2.1
    :cvar PTI3_2: DEPRECATED since SIRI 2.1
    :cvar PTI3_3: DEPRECATED since SIRI 2.1
    :cvar PTI3_4: DEPRECATED since SIRI 2.1
    :cvar PTI3_5: DEPRECATED since SIRI 2.1
    :cvar PTI3_6: DEPRECATED since SIRI 2.1
    :cvar PTI3_7: DEPRECATED since SIRI 2.1
    :cvar PTI3_8: DEPRECATED since SIRI 2.1
    :cvar PTI3_9: DEPRECATED since SIRI 2.1
    :cvar PTI3_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_COACH = "internationalCoach"
    NATIONAL_COACH = "nationalCoach"
    SHUTTLE_COACH = "shuttleCoach"
    REGIONAL_COACH = "regionalCoach"
    SPECIAL_COACH = "specialCoach"
    SCHOOL_COACH = "schoolCoach"
    SIGHTSEEING_COACH = "sightseeingCoach"
    TOURIST_COACH = "touristCoach"
    COMMUTER_COACH = "commuterCoach"
    INTERNATIONAL_COACH_SERVICE = "internationalCoachService"
    NATIONAL_COACH_SERVICE = "nationalCoachService"
    SHUTTLE_COACH_SERVICE = "shuttleCoachService"
    REGIONAL_COACH_SERVICE = "regionalCoachService"
    ADDITIONAL_COACH_SERVICE = "additionalCoachService"
    NIGHT_COACH_SERVICE = "nightCoachService"
    SPECIAL_COACH_SERVICE = "specialCoachService"
    SIGHTSEEING_COACH_SERVICE = "sightseeingCoachService"
    TOURIST_COACH_SERVICE = "touristCoachService"
    COMMUTER_COACH_SERVICE = "commuterCoachService"
    ON_DEMAND_SERVICE = "onDemandService"
    UNDEFINED_COACH_SERVICE = "undefinedCoachService"
    ALL_COACH_SERVICES = "allCoachServices"
    PTI3_0 = "pti3_0"
    PTI3_1 = "pti3_1"
    PTI3_2 = "pti3_2"
    PTI3_3 = "pti3_3"
    PTI3_4 = "pti3_4"
    PTI3_5 = "pti3_5"
    PTI3_6 = "pti3_6"
    PTI3_7 = "pti3_7"
    PTI3_8 = "pti3_8"
    PTI3_9 = "pti3_9"
    PTI3_255 = "pti3_255"
