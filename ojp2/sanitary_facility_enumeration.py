from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SanitaryFacilityEnumeration(Enum):
    """Values for Sanitary Facility: TPEG pti_table 23."""

    UNKNOWN = "unknown"
    PTI23_22 = "pti23_22"
    TOILET = "toilet"
    PTI23_23 = "pti23_23"
    NO_TOILET = "noToilet"
    SHOWER = "shower"
    WHEELCHAIR_ACCCESS_TOILET = "wheelchairAcccessToilet"
    BABY_CHANGE = "babyChange"
