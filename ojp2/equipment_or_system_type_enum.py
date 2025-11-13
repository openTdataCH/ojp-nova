from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class EquipmentOrSystemTypeEnum(Enum):
    AUTOMATED_TOLL_SYSTEM = "automatedTollSystem"
    EMERGENCY_ROADSIDE_TELEPHONES = "emergencyRoadsideTelephones"
    GALLERY_LIGHTS = "galleryLights"
    LANE_CONTROL_SIGNS = "laneControlSigns"
    LEVEL_CROSSING = "levelCrossing"
    MATRIX_SIGNS = "matrixSigns"
    RAMP_CONTROLS = "rampControls"
    ROADSIDE_COMMUNICATIONS_SYSTEM = "roadsideCommunicationsSystem"
    ROADSIDE_POWER_SYSTEM = "roadsidePowerSystem"
    SPEED_CONTROL_SIGNS = "speedControlSigns"
    STREET_LIGHTING = "streetLighting"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES = "tollGates"
    TRAFFIC_LIGHT_SETS = "trafficLightSets"
    TRAFFIC_SIGNALS = "trafficSignals"
    TUNNEL_LIGHTS = "tunnelLights"
    TUNNEL_VENTILATION = "tunnelVentilation"
    VARIABLE_MESSAGE_SIGNS = "variableMessageSigns"
    OTHER = "other"
