from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AccessibilityDetailsProfileEnumeration(Enum):
    """
    Allowed values for AccessibilityDetails.
    """
    VISUAL_IMPAIRMENT = "visualImpairment"
    AUDITORY_IMPAIRMENT = "auditoryImpairment"
    MOBILITY_IMPAIRMENT = "mobilityImpairment"
    BICYCLE = "bicycle"
    GENERAL = "general"
