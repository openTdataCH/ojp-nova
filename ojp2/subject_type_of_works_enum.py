from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class SubjectTypeOfWorksEnum(Enum):
    BRIDGE = "bridge"
    BURIED_CABLES = "buriedCables"
    BURIED_SERVICES = "buriedServices"
    CRASH_BARRIER = "crashBarrier"
    GALLERY = "gallery"
    GANTRY = "gantry"
    GAS_MAIN_WORK = "gasMainWork"
    INTERCHANGE = "interchange"
    JUNCTION = "junction"
    LEVEL_CROSSING = "levelCrossing"
    LIGHTING_SYSTEM = "lightingSystem"
    MEASUREMENT_EQUIPMENT = "measurementEquipment"
    NOISE_PROTECTION = "noiseProtection"
    ROAD = "road"
    ROADSIDE_DRAINS = "roadsideDrains"
    ROADSIDE_EMBANKMENT = "roadsideEmbankment"
    ROADSIDE_EQUIPMENT = "roadsideEquipment"
    ROAD_SIGNS = "roadSigns"
    ROUNDABOUT = "roundabout"
    TOLL_GATE = "tollGate"
    TUNNEL = "tunnel"
    WATER_MAIN = "waterMain"
    OTHER = "other"
