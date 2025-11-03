from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AssistanceFacilityEnumeration(Enum):
    """
    Values for Assistance Facility.
    """

    UNKNOWN = "unknown"
    POLICE = "police"
    FIRST_AID = "firstAid"
    SOS_POINT = "sosPoint"
    SPECIFIC_ASSISTANCE = "specificAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    BOARDING_ASSISTANCE = "boardingAssistance"
