from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ParkingFacilityEnumeration(Enum):
    """
    Values for Access Facility.
    """

    UNKNOWN = "unknown"
    CAR_PARK = "carPark"
    PARK_AND_RIDE_PARK = "parkAndRidePark"
    MOTORCYCLE_PARK = "motorcyclePark"
    CYCLE_PARK = "cyclePark"
    RENTAL_CAR_PARK = "rentalCarPark"
    COACH_PARK = "coachPark"
