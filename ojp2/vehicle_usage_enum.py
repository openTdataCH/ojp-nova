from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class VehicleUsageEnum(Enum):
    AGRICULTURAL = "agricultural"
    COMMERCIAL = "commercial"
    EMERGENCY_SERVICES = "emergencyServices"
    MILITARY = "military"
    NON_COMMERCIAL = "nonCommercial"
    PATROL = "patrol"
    RECOVERY_SERVICES = "recoveryServices"
    ROAD_MAINTENANCE_OR_CONSTRUCTION = "roadMaintenanceOrConstruction"
    ROAD_OPERATOR = "roadOperator"
    TAXI = "taxi"
