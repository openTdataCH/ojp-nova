from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RoadOperatorServiceDisruptionTypeEnum(Enum):
    EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE = "emergencyTelephoneNumberOutOfService"
    INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE = "informationServiceTelephoneNumberOutOfService"
    NO_TRAFFIC_OFFICER_PATROL_SERVICE = "noTrafficOfficerPatrolService"
