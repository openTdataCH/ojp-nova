from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RoadMaintenanceTypeEnum(Enum):
    CLEARANCE_WORK = "clearanceWork"
    CONTROLLED_AVALANCHE = "controlledAvalanche"
    INSTALLATION_WORK = "installationWork"
    GRASS_CUTTING_WORK = "grassCuttingWork"
    MAINTENANCE_WORK = "maintenanceWork"
    OVERHEAD_WORKS = "overheadWorks"
    REPAIR_WORK = "repairWork"
    RESURFACING_WORK = "resurfacingWork"
    ROAD_MARKING_WORK = "roadMarkingWork"
    ROADSIDE_WORK = "roadsideWork"
    ROADWORKS_CLEARANCE = "roadworksClearance"
    ROADWORKS = "roadworks"
    ROCK_FALL_PREVENTATIVE_MAINTENANCE = "rockFallPreventativeMaintenance"
    SALTING_IN_PROGRESS = "saltingInProgress"
    SNOWPLOUGHS_IN_USE = "snowploughsInUse"
    TREE_AND_VEGETATION_CUTTING_WORK = "treeAndVegetationCuttingWork"
    OTHER = "other"
