from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class NonWeatherRelatedRoadConditionTypeEnum(Enum):
    DIESEL_ON_ROAD = "dieselOnRoad"
    LEAVES_ON_ROAD = "leavesOnRoad"
    LOOSE_CHIPPINGS = "looseChippings"
    LOOSE_SAND_ON_ROAD = "looseSandOnRoad"
    MUD_ON_ROAD = "mudOnRoad"
    OIL_ON_ROAD = "oilOnRoad"
    PETROL_ON_ROAD = "petrolOnRoad"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"
