from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class WeatherRelatedRoadConditionTypeEnum(Enum):
    BLACK_ICE = "blackIce"
    DEEP_SNOW = "deepSnow"
    DRY = "dry"
    FREEZING_OF_WET_ROADS = "freezingOfWetRoads"
    FREEZING_PAVEMENTS = "freezingPavements"
    FREEZING_RAIN = "freezingRain"
    FRESH_SNOW = "freshSnow"
    ICE = "ice"
    ICE_BUILD_UP = "iceBuildUp"
    ICE_WITH_WHEEL_BAR_TRACKS = "iceWithWheelBarTracks"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS = "normalWinterConditionsForPedestrians"
    PACKED_SNOW = "packedSnow"
    ROAD_SURFACE_MELTING = "roadSurfaceMelting"
    SLIPPERY_ROAD = "slipperyRoad"
    SLUSH_ON_ROAD = "slushOnRoad"
    SLUSH_STRINGS = "slushStrings"
    SNOW_DRIFTS = "snowDrifts"
    SNOW_ON_PAVEMENT = "snowOnPavement"
    SNOW_ON_THE_ROAD = "snowOnTheRoad"
    SURFACE_WATER = "surfaceWater"
    WET = "wet"
    WET_AND_ICY_ROAD = "wetAndIcyRoad"
    WET_ICY_PAVEMENT = "wetIcyPavement"
    OTHER = "other"
