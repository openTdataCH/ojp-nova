from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EnvironmentReasonEnumeration(Enum):
    """
    Values for Environment incident reason types TPEG Pti18_4/TPEG Pti_22.

    :cvar PTI22_0:
    :cvar UNKNOWN: TPEG Pti22_0 unknown.
    :cvar PTI22_1:
    :cvar FOG: TPEG Pti22_1 fog.
    :cvar PTI22_2:
    :cvar ROUGH_SEA: TPEG Pti22_2 rough sea.
    :cvar PTI22_3:
    :cvar HEAVY_SNOW_FALL: TPEG Pti22_3 heavy snow fall.
    :cvar PTI22_3_ALIAS_1:
    :cvar DRIFTING_SNOW: drifting snow - Alias to TPEG Pti22_3
        heavySnowFall.
    :cvar PTI22_3_ALIAS_2:
    :cvar BLIZZARD_CONDITIONS: Blizzard Conditions - Alias to TPEG
        Pti22_3 heavySnowFall.
    :cvar PTI22_4:
    :cvar HEAVY_RAIN: TPEG Pti22_4 heavy rain.
    :cvar PTI22_5:
    :cvar STRONG_WINDS: TPEG Pti22_5 strong winds.
    :cvar PTI22_5_ALIAS_1:
    :cvar STORM_CONDITIONS: stormConditions alias to TPEG Pti22_5 strong
        winds.
    :cvar PTI22_5_ALIAS_2:
    :cvar STORM_DAMAGE: storm damage alias to TPEG Pti22_5 strong winds.
    :cvar PTI22_6:
    :cvar TIDAL_RESTRICTIONS: TPEG Pti22_6 tidal restrictions.
    :cvar PTI22_7:
    :cvar HIGH_TIDE: TPEG Pti22_7 high tide.
    :cvar PTI22_8:
    :cvar LOW_TIDE: TPEG Pti22_8 low tide.
    :cvar PTI22_9:
    :cvar ICE: TPEG Pti22_9 ice.
    :cvar PTI22_9_ALIAS_1:
    :cvar SLIPPERINESS: TPEG Pti22_9 ice.
    :cvar PTI22_9_ALIAS_2:
    :cvar ICE_DRIFT: TPEG Pti22_9 ice.
    :cvar PTI22_9_ALIAS_3:
    :cvar GLAZED_FROST: TPEG Pti22_9 ice.
    :cvar PTI22_10:
    :cvar FROZEN: TPEG Pti22_10 frozen.
    :cvar PTI22_11:
    :cvar HAIL: TPEG Pti22_11 hail.
    :cvar PTI22_11_ALIAS_1:
    :cvar SLEET: Sleet Alias to TPEG Pti22_11 hail.
    :cvar PTI22_12:
    :cvar HIGH_TEMPERATURES: TPEG Pti22_12 high temperatures.
    :cvar PTI22_13:
    :cvar FLOODING: TPEG Pti22_13 flooding.
    :cvar PTI22_14:
    :cvar WATERLOGGED: TPEG Pti22_14 waterlogged.
    :cvar PTI22_15:
    :cvar LOW_WATER_LEVEL: TPEG Pti22_15 low water level.
    :cvar PTI22_16:
    :cvar HIGH_WATER_LEVEL: TPEG Pti22_16 high water level.
    :cvar PTI22_17:
    :cvar FALLEN_LEAVES: TPEG Pti22_17 fallen leaves.
    :cvar PTI22_18:
    :cvar FALLEN_TREE: TPEG Pti22_18 fallen tree.
    :cvar PTI22_19:
    :cvar LANDSLIDE: TPEG Pti22_19 landslide.
    :cvar PTI22_255:
    :cvar UNDEFINED_ENVIRONMENTAL_PROBLEM: TPEG Pti22_255 undefined
        environmental problem.
    :cvar PTI22_255_ALIAS_1:
    :cvar LIGHTNING_STRIKE: lightningStrike alias to TPEG Pti22_255
        undefined environmental problem.
    :cvar PTI22_255_ALIAS_2:
    :cvar SEWER_OVERFLOW:
    :cvar PTI22_255_ALIAS_3:
    :cvar GRASS_FIRE:
    """
    PTI22_0 = "pti22_0"
    UNKNOWN = "unknown"
    PTI22_1 = "pti22_1"
    FOG = "fog"
    PTI22_2 = "pti22_2"
    ROUGH_SEA = "roughSea"
    PTI22_3 = "pti22_3"
    HEAVY_SNOW_FALL = "heavySnowFall"
    PTI22_3_ALIAS_1 = "pti22_3_Alias_1"
    DRIFTING_SNOW = "driftingSnow"
    PTI22_3_ALIAS_2 = "pti22_3_Alias_2"
    BLIZZARD_CONDITIONS = "blizzardConditions"
    PTI22_4 = "pti22_4"
    HEAVY_RAIN = "heavyRain"
    PTI22_5 = "pti22_5"
    STRONG_WINDS = "strongWinds"
    PTI22_5_ALIAS_1 = "pti22_5_Alias_1"
    STORM_CONDITIONS = "stormConditions"
    PTI22_5_ALIAS_2 = "pti22_5_Alias_2"
    STORM_DAMAGE = "stormDamage"
    PTI22_6 = "pti22_6"
    TIDAL_RESTRICTIONS = "tidalRestrictions"
    PTI22_7 = "pti22_7"
    HIGH_TIDE = "highTide"
    PTI22_8 = "pti22_8"
    LOW_TIDE = "lowTide"
    PTI22_9 = "pti22_9"
    ICE = "ice"
    PTI22_9_ALIAS_1 = "pti22_9_Alias_1"
    SLIPPERINESS = "slipperiness"
    PTI22_9_ALIAS_2 = "pti22_9_Alias_2"
    ICE_DRIFT = "iceDrift"
    PTI22_9_ALIAS_3 = "pti22_9_Alias_3"
    GLAZED_FROST = "glazedFrost"
    PTI22_10 = "pti22_10"
    FROZEN = "frozen"
    PTI22_11 = "pti22_11"
    HAIL = "hail"
    PTI22_11_ALIAS_1 = "pti22_11_Alias_1"
    SLEET = "sleet"
    PTI22_12 = "pti22_12"
    HIGH_TEMPERATURES = "highTemperatures"
    PTI22_13 = "pti22_13"
    FLOODING = "flooding"
    PTI22_14 = "pti22_14"
    WATERLOGGED = "waterlogged"
    PTI22_15 = "pti22_15"
    LOW_WATER_LEVEL = "lowWaterLevel"
    PTI22_16 = "pti22_16"
    HIGH_WATER_LEVEL = "highWaterLevel"
    PTI22_17 = "pti22_17"
    FALLEN_LEAVES = "fallenLeaves"
    PTI22_18 = "pti22_18"
    FALLEN_TREE = "fallenTree"
    PTI22_19 = "pti22_19"
    LANDSLIDE = "landslide"
    PTI22_255 = "pti22_255"
    UNDEFINED_ENVIRONMENTAL_PROBLEM = "undefinedEnvironmentalProblem"
    PTI22_255_ALIAS_1 = "pti22_255_Alias_1"
    LIGHTNING_STRIKE = "lightningStrike"
    PTI22_255_ALIAS_2 = "pti22_255_Alias_2"
    SEWER_OVERFLOW = "sewerOverflow"
    PTI22_255_ALIAS_3 = "pti22_255_Alias_3"
    GRASS_FIRE = "grassFire"
