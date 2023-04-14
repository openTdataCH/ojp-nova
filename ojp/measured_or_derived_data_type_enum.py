from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class MeasuredOrDerivedDataTypeEnum(Enum):
    HUMIDITY_INFORMATION = "humidityInformation"
    INDIVIDUAL_VEHICLE_MEASUREMENTS = "individualVehicleMeasurements"
    POLLUTION_INFORMATION = "pollutionInformation"
    PRECIPITATION_INFORMATION = "precipitationInformation"
    PRESSURE_INFORMATION = "pressureInformation"
    RADIATION_INFORMATION = "radiationInformation"
    ROAD_SURFACE_CONDITION_INFORMATION = "roadSurfaceConditionInformation"
    TEMPERATURE_INFORMATION = "temperatureInformation"
    TRAFFIC_CONCENTRATION = "trafficConcentration"
    TRAFFIC_FLOW = "trafficFlow"
    TRAFFIC_HEADWAY = "trafficHeadway"
    TRAFFIC_SPEED = "trafficSpeed"
    TRAFFIC_STATUS_INFORMATION = "trafficStatusInformation"
    TRAVEL_TIME_INFORMATION = "travelTimeInformation"
    VISIBILITY_INFORMATION = "visibilityInformation"
    WIND_INFORMATION = "windInformation"
