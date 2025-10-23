from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class InfrastructureDamageTypeEnum(Enum):
    BURST_PIPE = "burstPipe"
    BURST_WATER_MAIN = "burstWaterMain"
    COLLAPSED_SEWER = "collapsedSewer"
    DAMAGED_BRIDGE = "damagedBridge"
    DAMAGED_CRASH_BARRIER = "damagedCrashBarrier"
    DAMAGED_FLYOVER = "damagedFlyover"
    DAMAGED_GALLERY = "damagedGallery"
    DAMAGED_GANTRY = "damagedGantry"
    DAMAGED_ROAD_SURFACE = "damagedRoadSurface"
    DAMAGED_TUNNEL = "damagedTunnel"
    DAMAGED_VIADUCT = "damagedViaduct"
    FALLEN_POWER_CABLES = "fallenPowerCables"
    GAS_LEAK = "gasLeak"
    WEAK_BRIDGE = "weakBridge"
    OTHER = "other"
