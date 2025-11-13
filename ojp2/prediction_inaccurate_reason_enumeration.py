from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictionInaccurateReasonEnumeration(Enum):
    """
    Allowed values for PredictionInaccurateReason, i.e., possible reasons for a
    change in prediction (in)accuracy.

    :cvar VEHICLE_IN_TRAFFIC_JAM: Prediction is inaccurate because of a
        traffic jam.
    :cvar TECHNICAL_PROBLEM: Prediction is inaccurate because of
        technical problems.
    :cvar DISPATCH_ACTION: Prediction is inaccurate because of a
        despatching alteration.
    :cvar MISSING_UPDATE: Prediction is inaccurate because communication
        errors have prevented any updates.
    :cvar UNKNOWN: Prediction is inaccurate but the reason for an
        inaccurate prediction is unknown.
    """

    VEHICLE_IN_TRAFFIC_JAM = "vehicleInTrafficJam"
    TECHNICAL_PROBLEM = "technicalProblem"
    DISPATCH_ACTION = "dispatchAction"
    MISSING_UPDATE = "missingUpdate"
    UNKNOWN = "unknown"
