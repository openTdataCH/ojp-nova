from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class CarParkStatusEnum(Enum):
    CAR_PARK_CLOSED = "carParkClosed"
    ALL_CAR_PARKS_FULL = "allCarParksFull"
    CAR_PARK_FACILITY_FAULTY = "carParkFacilityFaulty"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_STATUS_UNKNOWN = "carParkStatusUnknown"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    MULTI_STORY_CAR_PARKS_FULL = "multiStoryCarParksFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    NO_PARK_AND_RIDE_INFORMATION = "noParkAndRideInformation"
    NO_PARKING_ALLOWED = "noParkingAllowed"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    NORMAL_PARKING_RESTRICTIONS_LIFTED = "normalParkingRestrictionsLifted"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    PARK_AND_RIDE_SERVICE_NOT_OPERATING = "parkAndRideServiceNotOperating"
    PARK_AND_RIDE_SERVICE_OPERATING = "parkAndRideServiceOperating"
    SPECIAL_PARKING_RESTRICTIONS_IN_FORCE = "specialParkingRestrictionsInForce"
