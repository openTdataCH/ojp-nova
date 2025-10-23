from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class MaintenanceVehicleActionsEnum(Enum):
    MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW = "maintenanceVehiclesMergingIntoTrafficFlow"
    SALT_AND_GRIT_SPREADING = "saltAndGritSpreading"
    SLOW_MOVING = "slowMoving"
    SNOW_CLEARING = "snowClearing"
    STOPPING_TO_SERVICE_EQUIPMENTS = "stoppingToServiceEquipments"
