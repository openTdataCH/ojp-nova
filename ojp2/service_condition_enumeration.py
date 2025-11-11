from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ServiceConditionEnumeration(Enum):
    """
    Values for TPEG Pts43 ServiceStatus, with additional values from Pti013.

    :cvar UNKNOWN: TPEG Pts43_0, unknown
    :cvar DELAY: TPEG Pts43_1, delay
    :cvar MINOR_DELAYS: TPEG Pts43_2, minor delays
    :cvar MAJOR_DELAYS: TPEG Pts43_3, major delays
    :cvar OPERATION_TIME_EXTENSION: TPEG Pts43_4, operation time
        extension
    :cvar ON_TIME: TPEG Pts43_5, on time
    :cvar DISTURBANCE_RECTIFIED: TPEG Pts43_6, disturbance rectified
    :cvar CHANGE_OF_PLATFORM: TPEG Pts43_7, change of platform
    :cvar LINE_CANCELLATION: TPEG Pts43_8, line cancellation
    :cvar TRIP_CANCELLATION: TPEG Pts43_9, trip cancellation
    :cvar BOARDING: TPEG Pts43_10, boarding
    :cvar GO_TO_GATE: TPEG Pts43_11, go to gate
    :cvar STOP_CANCELLED: TPEG Pts43_12, stop cancelled
    :cvar STOP_MOVED: TPEG Pts43_13, stop moved
    :cvar STOP_ON_DEMAND: TPEG Pts43_14, stop on demand
    :cvar ADDITIONAL_STOP: TPEG Pts43_15, additional stop
    :cvar SUBSTITUTED_STOP: TPEG Pts43_16, substituted stop
    :cvar DIVERTED: TPEG Pts43_17, diverted
    :cvar DISRUPTION: TPEG Pts43_18, disruption
    :cvar LIMITED_OPERATION: TPEG Pts43_19, limited operation
    :cvar DISCONTINUED_OPERATION: TPEG Pts43_20, discontinued operation
    :cvar IRREGULAR_TRAFFIC: TPEG Pts43_21, irregular traffic
    :cvar WAGON_ORDER_CHANGED: TPEG Pts43_22, wagon order changed
    :cvar TRAIN_SHORTENED: TPEG Pts43_23, train shortened
    :cvar ADDITIONAL_RIDE: TPEG Pts43_24, additional ride
    :cvar REPLACEMENT_RIDE: TPEG Pts43_25, replacement ride
    :cvar TEMPORARILY_NON_STOPPING: TPEG Pts43_26, temporarily non-
        stopping
    :cvar TEMPORARY_STOPPLACE: TPEG Pts43_27, temporary stopplace
    :cvar UNDEFINED_STATUS: TPEG Pts43_255, undefined status
    :cvar ALTERED: TPEG Pti13_1, DEPRECATED since SIRI 2.1
    :cvar CANCELLED: TPEG Pti13_2, DEPRECATED since SIRI 2.1
    :cvar DELAYED: TPEG Pti13_3, DEPRECATED since SIRI 2.1
    :cvar NO_SERVICE: TPEG Pti13_5, DEPRECATED since SIRI 2.1
    :cvar DISRUPTED: TPEG Pti13_6, DEPRECATED since SIRI 2.1
    :cvar ADDITIONAL_SERVICE: TPEG Pti13_7, DEPRECATED since SIRI 2.1
    :cvar SPECIAL_SERVICE: TPEG Pti13_8, DEPRECATED since SIRI 2.1
    :cvar NORMAL_SERVICE: TPEG Pti13_10, DEPRECATED since SIRI 2.1
    :cvar INTERMITTENT_SERVICE: TPEG Pti13_11, DEPRECATED since SIRI 2.1
    :cvar SHORT_FORMED_SERVICE: TPEG Pti13_12, DEPRECATED since SIRI 2.1
    :cvar FULL_LENGTH_SERVICE: TPEG Pti13_13, DEPRECATED since SIRI 2.1
    :cvar EXTENDED_SERVICE: TPEG Pti13_14, DEPRECATED since SIRI 2.1
    :cvar SPLITTING_TRAIN: TPEG Pti13_15, DEPRECATED since SIRI 2.1
    :cvar REPLACEMENT_TRANSPORT: TPEG Pti13_16, DEPRECATED since SIRI
        2.1
    :cvar ARRIVES_EARLY: TPEG Pti13_17, DEPRECATED since SIRI 2.1
    :cvar SHUTTLE_SERVICE: TPEG Pti13_18, DEPRECATED since SIRI 2.1
    :cvar REPLACEMENT_SERVICE: TPEG Pti13_19, DEPRECATED since SIRI 2.1
    :cvar UNDEFINED_SERVICE_INFORMATION: TPEG Pti13_255, DEPRECATED
        since SIRI 2.1
    """

    UNKNOWN = "unknown"
    DELAY = "delay"
    MINOR_DELAYS = "minorDelays"
    MAJOR_DELAYS = "majorDelays"
    OPERATION_TIME_EXTENSION = "operationTimeExtension"
    ON_TIME = "onTime"
    DISTURBANCE_RECTIFIED = "disturbanceRectified"
    CHANGE_OF_PLATFORM = "changeOfPlatform"
    LINE_CANCELLATION = "lineCancellation"
    TRIP_CANCELLATION = "tripCancellation"
    BOARDING = "boarding"
    GO_TO_GATE = "goToGate"
    STOP_CANCELLED = "stopCancelled"
    STOP_MOVED = "stopMoved"
    STOP_ON_DEMAND = "stopOnDemand"
    ADDITIONAL_STOP = "additionalStop"
    SUBSTITUTED_STOP = "substitutedStop"
    DIVERTED = "diverted"
    DISRUPTION = "disruption"
    LIMITED_OPERATION = "limitedOperation"
    DISCONTINUED_OPERATION = "discontinuedOperation"
    IRREGULAR_TRAFFIC = "irregularTraffic"
    WAGON_ORDER_CHANGED = "wagonOrderChanged"
    TRAIN_SHORTENED = "trainShortened"
    ADDITIONAL_RIDE = "additionalRide"
    REPLACEMENT_RIDE = "replacementRide"
    TEMPORARILY_NON_STOPPING = "temporarilyNonStopping"
    TEMPORARY_STOPPLACE = "temporaryStopplace"
    UNDEFINED_STATUS = "undefinedStatus"
    ALTERED = "altered"
    CANCELLED = "cancelled"
    DELAYED = "delayed"
    NO_SERVICE = "noService"
    DISRUPTED = "disrupted"
    ADDITIONAL_SERVICE = "additionalService"
    SPECIAL_SERVICE = "specialService"
    NORMAL_SERVICE = "normalService"
    INTERMITTENT_SERVICE = "intermittentService"
    SHORT_FORMED_SERVICE = "shortFormedService"
    FULL_LENGTH_SERVICE = "fullLengthService"
    EXTENDED_SERVICE = "extendedService"
    SPLITTING_TRAIN = "splittingTrain"
    REPLACEMENT_TRANSPORT = "replacementTransport"
    ARRIVES_EARLY = "arrivesEarly"
    SHUTTLE_SERVICE = "shuttleService"
    REPLACEMENT_SERVICE = "replacementService"
    UNDEFINED_SERVICE_INFORMATION = "undefinedServiceInformation"
