from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class SourceTypeEnum(Enum):
    AUTOMOBILE_CLUB_PATROL = "automobileClubPatrol"
    CAMERA_OBSERVATION = "cameraObservation"
    FREIGHT_VEHICLE_OPERATOR = "freightVehicleOperator"
    INDUCTION_LOOP_MONITORING_STATION = "inductionLoopMonitoringStation"
    INFRARED_MONITORING_STATION = "infraredMonitoringStation"
    MICROWAVE_MONITORING_STATION = "microwaveMonitoringStation"
    MOBILE_TELEPHONE_CALLER = "mobileTelephoneCaller"
    NON_POLICE_EMERGENCY_SERVICE_PATROL = "nonPoliceEmergencyServicePatrol"
    OTHER_INFORMATION = "otherInformation"
    OTHER_OFFICIAL_VEHICLE = "otherOfficialVehicle"
    POLICE_PATROL = "policePatrol"
    PRIVATE_BREAKDOWN_SERVICE = "privateBreakdownService"
    PUBLIC_AND_PRIVATE_UTILITIES = "publicAndPrivateUtilities"
    REGISTERED_MOTORIST_OBSERVER = "registeredMotoristObserver"
    ROAD_AUTHORITIES = "roadAuthorities"
    ROAD_OPERATOR_PATROL = "roadOperatorPatrol"
    ROADSIDE_TELEPHONE_CALLER = "roadsideTelephoneCaller"
    SPOTTER_AIRCRAFT = "spotterAircraft"
    TRAFFIC_MONITORING_STATION = "trafficMonitoringStation"
    TRANSIT_OPERATOR = "transitOperator"
    VEHICLE_PROBE_MEASUREMENT = "vehicleProbeMeasurement"
    VIDEO_PROCESSING_MONITORING_STATION = "videoProcessingMonitoringStation"
