from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TransitServiceInformationEnum(Enum):
    CANCELLATIONS = "cancellations"
    DELAY_DUE_TO_BAD_WEATHER = "delayDueToBadWeather"
    DELAY_DUE_TO_REPAIRS = "delayDueToRepairs"
    DELAYED_UNTIL_FURTHER_NOTICE = "delayedUntilFurtherNotice"
    DELAYS_DUE_TO_FLOTSAM = "delaysDueToFlotsam"
    DEPARTURE_ON_SCHEDULE = "departureOnSchedule"
    FERRY_REPLACED_BY_ICE_ROAD = "ferryReplacedByIceRoad"
    FREE_SHUTTLE_SERVICE_OPERATING = "freeShuttleServiceOperating"
    INFORMATION_SERVICE_NOT_AVAILABLE = "informationServiceNotAvailable"
    IRREGULAR_SERVICE_DELAYS = "irregularServiceDelays"
    LOAD_CAPACITY_CHANGED = "loadCapacityChanged"
    RESTRICTIONS_FOR_LONGER_VEHICLES = "restrictionsForLongerVehicles"
    SERVICE_DELAYS = "serviceDelays"
    SERVICE_DELAYS_OF_UNCERTAIN_DURATION = "serviceDelaysOfUncertainDuration"
    SERVICE_FULLY_BOOKED = "serviceFullyBooked"
    SERVICE_NOT_OPERATING = "serviceNotOperating"
    SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE = "serviceNotOperatingSubstituteServiceAvailable"
    SERVICE_SUSPENDED = "serviceSuspended"
    SERVICE_WITHDRAWN = "serviceWithdrawn"
    SHUTTLE_SERVICE_OPERATING = "shuttleServiceOperating"
    TEMPORARY_CHANGES_TO_TIMETABLES = "temporaryChangesToTimetables"
    OTHER = "other"
