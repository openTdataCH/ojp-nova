from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ReservedSpaceFacilityEnumeration(Enum):
    """
    Values for Reserved Space Facility.
    """
    UNKNOWN = "unknown"
    LOUNGE = "lounge"
    HALL = "hall"
    MEETINGPOINT = "meetingpoint"
    GROUP_POINT = "groupPoint"
    RECEPTION = "reception"
    SHELTER = "shelter"
    SEATS = "seats"
