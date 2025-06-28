from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class EnvironmentalObstructionTypeEnum(Enum):
    AVALANCHES = "avalanches"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    FALLEN_TREES = "fallenTrees"
    FALLING_ICE = "fallingIce"
    FALLING_LIGHT_ICE_OR_SNOW = "fallingLightIceOrSnow"
    FLASH_FLOODS = "flashFloods"
    FLOODING = "flooding"
    FOREST_FIRE = "forestFire"
    GRASS_FIRE = "grassFire"
    LANDSLIPS = "landslips"
    MUD_SLIDE = "mudSlide"
    SEWER_OVERFLOW = "sewerOverflow"
    ROCKFALLS = "rockfalls"
    SERIOUS_FIRE = "seriousFire"
    SMOKE_OR_FUMES = "smokeOrFumes"
    STORM_DAMAGE = "stormDamage"
    SUBSIDENCE = "subsidence"
    OTHER = "other"
