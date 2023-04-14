from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EnvironmentSubReasonEnumeration(Enum):
    """
    Values for Environment incident subreason types.

    :cvar UNKNOWN: TPEG Pti22_0 unknown.
    :cvar FOG: TPEG Pti22_1 fog.
    :cvar ROUGH_SEA: TPEG Pti22_2 rough sea.
    :cvar HEAVY_SNOW_FALL:
    :cvar DRIFTING_SNOW: drifting snow - Alias to TPEG Pti22_3
        heavySnowFall.
    :cvar HEAVY_RAIN: TPEG Pti22_4 heavy rain.
    :cvar BLIZZARD_CONDITIONS: Blizzard Conditions - Alias to TPEG
        Pti22_3 heavySnowFall.
    :cvar STRONG_WINDS: TPEG Pti22_5 strong winds.
    :cvar STORM_CONDITIONS: stormConditions alias to TPEG Pti22_5 strong
        winds.
    :cvar STORM_DAMAGE: storm damage alias to TPEG Pti22_5 strong winds.
    :cvar TIDAL_RESTRICTIONS: TPEG Pti22_6 tidal restrictions.
    :cvar HIGH_TIDE: TPEG Pti22_7 high tide.
    :cvar LOW_TIDE: TPEG Pti22_8 low tide.
    :cvar ICE: TPEG Pti22_9 ice.
    :cvar SLIPPERINESS: TPEG Pti22_9 ice.
    :cvar ICE_DRIFT: TPEG Pti22_9 ice.
    :cvar GLAZED_FROST: TPEG Pti22_9 ice.
    :cvar FROZEN: TPEG Pti22_10 frozen.
    :cvar HAIL: TPEG Pti22_11 hail.
    :cvar SLEET: Sleet Alias to TPEG Pti22_11 hail.
    :cvar HIGH_TEMPERATURES: TPEG Pti22_12 high temperatures.
    :cvar FLOODING: TPEG Pti22_13 flooding.
    :cvar WATERLOGGED: TPEG Pti22_14 waterlogged.
    :cvar LOW_WATER_LEVEL: TPEG Pti22_15 low water level.
    :cvar HIGH_WATER_LEVEL: TPEG Pti22_16 high water level.
    :cvar FALLEN_LEAVES: TPEG Pti22_17 fallen leaves.
    :cvar FALLEN_TREE: TPEG Pti22_18 fallen tree.
    :cvar LANDSLIDE: TPEG Pti22_19 landslide.
    :cvar UNDEFINED_ENVIRONMENTAL_PROBLEM: TPEG Pti22_255 undefined
        environmental problem.
    :cvar SEWER_OVERFLOW:
    :cvar GRASS_FIRE:
    :cvar LIGHTENING_STRIKE:
    :cvar AVALANCHES:
    :cvar FLASH_FLOODS:
    :cvar MUDSLIP:
    :cvar ROCKFALLS:
    :cvar SUBSIDENCE:
    :cvar EARTHQUAKE_DAMAGE:
    """
    UNKNOWN = "unknown"
    FOG = "fog"
    ROUGH_SEA = "roughSea"
    HEAVY_SNOW_FALL = "heavySnowFall"
    DRIFTING_SNOW = "driftingSnow"
    HEAVY_RAIN = "heavyRain"
    BLIZZARD_CONDITIONS = "blizzardConditions"
    STRONG_WINDS = "strongWinds"
    STORM_CONDITIONS = "stormConditions"
    STORM_DAMAGE = "stormDamage"
    TIDAL_RESTRICTIONS = "tidalRestrictions"
    HIGH_TIDE = "highTide"
    LOW_TIDE = "lowTide"
    ICE = "ice"
    SLIPPERINESS = "slipperiness"
    ICE_DRIFT = "iceDrift"
    GLAZED_FROST = "glazedFrost"
    FROZEN = "frozen"
    HAIL = "hail"
    SLEET = "sleet"
    HIGH_TEMPERATURES = "highTemperatures"
    FLOODING = "flooding"
    WATERLOGGED = "waterlogged"
    LOW_WATER_LEVEL = "lowWaterLevel"
    HIGH_WATER_LEVEL = "highWaterLevel"
    FALLEN_LEAVES = "fallenLeaves"
    FALLEN_TREE = "fallenTree"
    LANDSLIDE = "landslide"
    UNDEFINED_ENVIRONMENTAL_PROBLEM = "undefinedEnvironmentalProblem"
    SEWER_OVERFLOW = "sewerOverflow"
    GRASS_FIRE = "grassFire"
    LIGHTENING_STRIKE = "lighteningStrike"
    AVALANCHES = "avalanches"
    FLASH_FLOODS = "flashFloods"
    MUDSLIP = "mudslip"
    ROCKFALLS = "rockfalls"
    SUBSIDENCE = "subsidence"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
