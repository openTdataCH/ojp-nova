from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class FeasibilityEnumeration(Enum):
    """
    Allowed values for the feasibility of a TRIP or part of a TRIP.
    """
    ALL_ACCESS_FEATURES_AVAILABLE = "allAccessFeaturesAvailable"
    ACCESS_FEATURE_NOT_AVAILABLE = "accessFeatureNotAvailable"
    ACCESS_FEATURE_PARTIALLY_AVAILABLE = "accessFeaturePartiallyAvailable"
    ACCESS_FEATURE_WITH_UNKNOWN_AVAILABILITY = "accessFeatureWithUnknownAvailability"
    SEE_SITUATIONS = "seeSituations"
