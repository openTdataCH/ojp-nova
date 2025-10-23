from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class GeneralNetworkManagementTypeEnum(Enum):
    BRIDGE_SWING_IN_OPERATION = "bridgeSwingInOperation"
    CONVOY_SERVICE = "convoyService"
    OBSTACLE_SIGNALLING = "obstacleSignalling"
    RAMP_METERING_IN_OPERATION = "rampMeteringInOperation"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES_OPEN = "tollGatesOpen"
    TRAFFIC_BEING_MANUALLY_DIRECTED = "trafficBeingManuallyDirected"
    TRAFFIC_HELD = "trafficHeld"
    OTHER = "other"
