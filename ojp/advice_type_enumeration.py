from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AdviceTypeEnumeration(Enum):
    """Values for TPEG Pts039 - AdviceType, with some additional values

    :cvar UNKNOWN: TPEG Pts39_0, unknown
    :cvar USE_REPLACEMENT_BUS: TPEG Pts39_1, use replacement bus
    :cvar USE_REPLACEMENT_TRAIN: TPEG Pts39_2, use replacement train
    :cvar USE_ALTERNATIVE_ROUTE: TPEG Pts39_3, use the alternative route
    :cvar GO_ON_FOOT: TPEG Pts39_4, go on foot
    :cvar DANGER_LEAVE_STATION: TPEG Pts39_5, please leave the station!
        Danger!
    :cvar NO_MEANS_OF_TRAVEL: TPEG Pts39_6, no means of travel
    :cvar USE_DIFFERENT_STOPS: TPEG Pts39_7, use different stops
    :cvar USE_ALTERNATIVE_STOP: TPEG Pts39_8, use alternative stop
    :cvar DANGER_DO_NOT_LEAVE_VEHICLE: TPEG Pts39_9, do not leave
        vehicle! Danger!
    :cvar TAKE_ADVICE_ANNOUNCEMENTS: TPEG Pts39_10, take advice from
        announcements
    :cvar TAKE_ADVICE_PERSONNEL: TPEG Pts39_11, take advice from
        personnel
    :cvar OBEY_ADVICE_POLICE: TPEG Pts39_12, obey advice from police
    :cvar USE_OTHER_PT: use other PT services
    :cvar USE_INTERCHANGE: use interchange
    :cvar NO_ADVICE: no advice
    :cvar UNDEFINED_ADVICE: TPEG Pts39_255, undefined advice
    :cvar TAKE_DETOUR: take detour
    :cvar USE_ALTERNATIVE_ACCESS: change accessibility
    """
    UNKNOWN = "unknown"
    USE_REPLACEMENT_BUS = "useReplacementBus"
    USE_REPLACEMENT_TRAIN = "useReplacementTrain"
    USE_ALTERNATIVE_ROUTE = "useAlternativeRoute"
    GO_ON_FOOT = "goOnFoot"
    DANGER_LEAVE_STATION = "dangerLeaveStation"
    NO_MEANS_OF_TRAVEL = "noMeansOfTravel"
    USE_DIFFERENT_STOPS = "useDifferentStops"
    USE_ALTERNATIVE_STOP = "useAlternativeStop"
    DANGER_DO_NOT_LEAVE_VEHICLE = "dangerDoNotLeaveVehicle"
    TAKE_ADVICE_ANNOUNCEMENTS = "takeAdviceAnnouncements"
    TAKE_ADVICE_PERSONNEL = "takeAdvicePersonnel"
    OBEY_ADVICE_POLICE = "obeyAdvicePolice"
    USE_OTHER_PT = "useOtherPT"
    USE_INTERCHANGE = "useInterchange"
    NO_ADVICE = "noAdvice"
    UNDEFINED_ADVICE = "undefinedAdvice"
    TAKE_DETOUR = "takeDetour"
    USE_ALTERNATIVE_ACCESS = "useAlternativeAccess"
