from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ServiceConditionEnumeration(Enum):
    """Values for Service Condition.

    Corresponds to TPEG Pti13 Service Condition values.

    :cvar PTI13_0:
    :cvar UNKNOWN: TPEG Pti13_unknown.
    :cvar PTI13_1:
    :cvar ALTERED: TPEG Pti13_altered.
    :cvar PTI13_2:
    :cvar CANCELLED: TPEG Pti13_cancelled.
    :cvar PTI13_3:
    :cvar DELAYED: TPEG Pti13_delayed.
    :cvar PTI13_4:
    :cvar DIVERTED: TPEG Pti13_diverted.
    :cvar PTI13_5:
    :cvar NO_SERVICE: TPEG Pti13_no service.
    :cvar PTI13_6:
    :cvar DISRUPTED: TPEG Pti13_disrupted.
    :cvar PTI13_7:
    :cvar ADDITIONAL_SERVICE: TPEG Pti13_additional service.
    :cvar PTI13_8:
    :cvar SPECIAL_SERVICE: TPEG Pti13_special service.
    :cvar PTI13_9:
    :cvar ON_TIME: TPEG Pti13_on time.
    :cvar PTI13_10:
    :cvar NORMAL_SERVICE: TPEG Pti13_normal service.
    :cvar PTI13_11:
    :cvar INTERMITTENT_SERVICE: TPEG Pti13_intermittent service.
    :cvar PTI13_12:
    :cvar SHORT_FORMED_SERVICE: TPEG Pti13_short formed service.
    :cvar PTI13_13:
    :cvar FULL_LENGTH_SERVICE: TPEG Pti13_full length service.
    :cvar PTI13_14:
    :cvar EXTENDED_SERVICE: TPEG Pti13_extended service.
    :cvar PTI13_15:
    :cvar SPLITTING_TRAIN: TPEG Pti13_splitting train.
    :cvar PTI13_16:
    :cvar REPLACEMENT_TRANSPORT: TPEG Pti13_replacement transport.
    :cvar PTI13_17:
    :cvar ARRIVES_EARLY: TPEG Pti13_arrives early.
    :cvar PTI13_18:
    :cvar SHUTTLE_SERVICE: TPEG Pti13_shuttle service.
    :cvar PTI13_19:
    :cvar REPLACEMENT_SERVICE: TPEG Pti13_replacement service.
    :cvar PTI13_255:
    :cvar UNDEFINED_SERVICE_INFORMATION: TPEG Pti13_Undefined service
        information.
    """
    PTI13_0 = "pti13_0"
    UNKNOWN = "unknown"
    PTI13_1 = "pti13_1"
    ALTERED = "altered"
    PTI13_2 = "pti13_2"
    CANCELLED = "cancelled"
    PTI13_3 = "pti13_3"
    DELAYED = "delayed"
    PTI13_4 = "pti13_4"
    DIVERTED = "diverted"
    PTI13_5 = "pti13_5"
    NO_SERVICE = "noService"
    PTI13_6 = "pti13_6"
    DISRUPTED = "disrupted"
    PTI13_7 = "pti13_7"
    ADDITIONAL_SERVICE = "additionalService"
    PTI13_8 = "pti13_8"
    SPECIAL_SERVICE = "specialService"
    PTI13_9 = "pti13_9"
    ON_TIME = "onTime"
    PTI13_10 = "pti13_10"
    NORMAL_SERVICE = "normalService"
    PTI13_11 = "pti13_11"
    INTERMITTENT_SERVICE = "intermittentService"
    PTI13_12 = "pti13_12"
    SHORT_FORMED_SERVICE = "shortFormedService"
    PTI13_13 = "pti13_13"
    FULL_LENGTH_SERVICE = "fullLengthService"
    PTI13_14 = "pti13_14"
    EXTENDED_SERVICE = "extendedService"
    PTI13_15 = "pti13_15"
    SPLITTING_TRAIN = "splittingTrain"
    PTI13_16 = "pti13_16"
    REPLACEMENT_TRANSPORT = "replacementTransport"
    PTI13_17 = "pti13_17"
    ARRIVES_EARLY = "arrivesEarly"
    PTI13_18 = "pti13_18"
    SHUTTLE_SERVICE = "shuttleService"
    PTI13_19 = "pti13_19"
    REPLACEMENT_SERVICE = "replacementService"
    PTI13_255 = "pti13_255"
    UNDEFINED_SERVICE_INFORMATION = "undefinedServiceInformation"
