from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AccommodationFacilityEnumeration(Enum):
    """Values for Accomodation Facility: TPEG pti_table 23."""

    UNKNOWN = "unknown"
    PTI23_3 = "pti23_3"
    SLEEPER = "sleeper"
    PTI23_4 = "pti23_4"
    COUCHETTE = "couchette"
    PTI23_5 = "pti23_5"
    SPECIAL_SEATING = "specialSeating"
    PTI23_11 = "pti23_11"
    FREE_SEATING = "freeSeating"
    PTI23_12 = "pti23_12"
    RECLINING_SEATS = "recliningSeats"
    PTI23_13 = "pti23_13"
    BABY_COMPARTMENT = "babyCompartment"
    FAMILY_CARRIAGE = "familyCarriage"
