from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RailSubmodesOfTransportEnumeration(Enum):
    """Values for Rail ModesOfTransport: TPEG pti_table_02, pts_table_102 "RailwayService" and train link loc_table_13.

    :cvar UNKNOWN: TPEG Pts102_0 - submode of transport is not known to
        the source system.
    :cvar LOCAL:
    :cvar HIGH_SPEED_RAIL: (SIRI 2.1)
    :cvar SUBURBAN_RAILWAY:
    :cvar REGIONAL_RAIL:
    :cvar INTERREGIONAL_RAIL: (SIRI 2.1)
    :cvar LONG_DISTANCE: (SIRI 2.1)
    :cvar INTERNATIONAL:
    :cvar SLEEPER_RAIL_SERVICE: TPEG Pts105_6
    :cvar NIGHT_RAIL: (SIRI 2.1)
    :cvar CAR_TRANSPORT_RAIL_SERVICE:
    :cvar TOURIST_RAILWAY:
    :cvar AIRPORT_LINK_RAIL: (SIRI 2.1)
    :cvar RAIL_SHUTTLE:
    :cvar REPLACEMENT_RAIL_SERVICE: TPEG Pts105_13
    :cvar SPECIAL_TRAIN: (SIRI 2.1)
    :cvar CROSS_COUNTRY_RAIL: (SIRI 2.1)
    :cvar RACK_AND_PINION_RAILWAY:
    :cvar HIGH_SPEED_RAIL_SERVICE: TPEG Pts102_1 - see also
        'highSpeedRail'.
    :cvar LONG_DISTANCE_INTERNATIONAL_RAIL_SERVICE: TPEG Pts102_2 (SIRI
        2.1) - see also 'international'.
    :cvar LONG_DISTANCE_RAIL_SERVICE: TPEG Pts102_3 (SIRI 2.1) - see
        also 'longDistance'.
    :cvar INTER_REGIONAL_EXPRESS_RAIL_SERVICE: TPEG Pts102_4 (SIRI 2.1)
    :cvar INTER_REGIONAL_RAIL_SERVICE: TPEG Pts105_5 - see also
        'interregionalRail'.
    :cvar REGIONAL_EXPRESS_RAIL_SERVICE: TPEG Pts105_7 (SIRI 2.1)
    :cvar REGIONAL_RAIL_SERVICE: TPEG Pts105_8 (SIRI 2.1) - see also
        'regionalRail'.
    :cvar TOURIST_RAILWAY_SERVICE: TPEG Pts105_9 (SIRI 2.1) - see also
        'touristRailway'.
    :cvar RAIL_SHUTTLE_SERVICE: TPEG Pts105_10 (SIRI 2.1) - see also
        'railShuttle'.
    :cvar SUBURBAN_RAIL_SERVICE: TPEG Pts105_11 (SIRI 2.1)
    :cvar SUBURBAN_NIGHT_RAIL_SERVICE: TPEG Pts105_12 (SIRI 2.1) - see
        also 'nightRail'.
    :cvar SPECIAL_RAIL_SERVICE: TPEG Pts105_14 (SIRI 2.1) - see also
        'specialTrain'.
    :cvar LORRY_TRANSPORT_RAIL_SERVICE: TPEG Pts105_15
    :cvar VEHICLE_TRANSPORT_RAIL_SERVICE: TPEG Pts105_17 (SIRI 2.1) -
        see also 'vehicleRailTransportService'.
    :cvar VEHICLE_TUNNEL_TRANSPORT_RAIL_SERVICE: TPEG Pts105_18 (SIRI
        2.1)
    :cvar ADDITIONAL_RAIL_SERVICE: TPEG Pts105_19 (SIRI 2.1) - see also
        'additionalTrainService'.
    :cvar UNDEFINED_RAIL_SERVICE: TPEG Pts105_255 (SIRI 2.1) - see also
        'undefined'.
    :cvar LONG_DISTANCE_TRAIN: See also 'longDistance'.
    :cvar SPECIAL_TRAIN_SERVICE:
    :cvar CROSS_COUNTRY_RAIL_SERVICE:
    :cvar VEHICLE_RAIL_TRANSPORT_SERVICE:
    :cvar ADDITIONAL_TRAIN_SERVICE:
    :cvar ALL_RAIL_SERVICES:
    :cvar UNDEFINED: Submode of transport is not supported in this list.
    :cvar INTERBATIONAL: DEPRECATED since SIRI 2.1
    :cvar PTI2_0: DEPRECATED since SIRI 2.1
    :cvar PTI2_1: DEPRECATED since SIRI 2.1
    :cvar PTI2_2: DEPRECATED since SIRI 2.1
    :cvar PTI2_3: DEPRECATED since SIRI 2.1
    :cvar PTI2_4: DEPRECATED since SIRI 2.1
    :cvar PTI2_5: DEPRECATED since SIRI 2.1
    :cvar PTI2_6: DEPRECATED since SIRI 2.1
    :cvar PTI2_7: DEPRECATED since SIRI 2.1
    :cvar PTI2_8: DEPRECATED since SIRI 2.1
    :cvar PTI2_9: DEPRECATED since SIRI 2.1
    :cvar PTI2_10: DEPRECATED since SIRI 2.1
    :cvar PTI2_11: DEPRECATED since SIRI 2.1
    :cvar PTI2_12: DEPRECATED since SIRI 2.1
    :cvar PTI2_13: DEPRECATED since SIRI 2.1
    :cvar PTI2_14: DEPRECATED since SIRI 2.1
    :cvar PTI2_15: DEPRECATED since SIRI 2.1
    :cvar PTI2_16: DEPRECATED since SIRI 2.1
    :cvar PTI2_17: DEPRECATED since SIRI 2.1
    :cvar PTI2_255: DEPRECATED since SIRI 2.1
    :cvar LOC13_0: DEPRECATED since SIRI 2.1
    :cvar LOC13_1: DEPRECATED since SIRI 2.1
    :cvar LOC13_2: DEPRECATED since SIRI 2.1
    :cvar LOC13_3: DEPRECATED since SIRI 2.1
    :cvar LOC13_4: DEPRECATED since SIRI 2.1
    :cvar LOC13_5: DEPRECATED since SIRI 2.1
    :cvar LOC13_6: DEPRECATED since SIRI 2.1
    :cvar LOC13_7: DEPRECATED since SIRI 2.1
    :cvar LOC13_8: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    LOCAL = "local"
    HIGH_SPEED_RAIL = "highSpeedRail"
    SUBURBAN_RAILWAY = "suburbanRailway"
    REGIONAL_RAIL = "regionalRail"
    INTERREGIONAL_RAIL = "interregionalRail"
    LONG_DISTANCE = "longDistance"
    INTERNATIONAL = "international"
    SLEEPER_RAIL_SERVICE = "sleeperRailService"
    NIGHT_RAIL = "nightRail"
    CAR_TRANSPORT_RAIL_SERVICE = "carTransportRailService"
    TOURIST_RAILWAY = "touristRailway"
    AIRPORT_LINK_RAIL = "airportLinkRail"
    RAIL_SHUTTLE = "railShuttle"
    REPLACEMENT_RAIL_SERVICE = "replacementRailService"
    SPECIAL_TRAIN = "specialTrain"
    CROSS_COUNTRY_RAIL = "crossCountryRail"
    RACK_AND_PINION_RAILWAY = "rackAndPinionRailway"
    HIGH_SPEED_RAIL_SERVICE = "highSpeedRailService"
    LONG_DISTANCE_INTERNATIONAL_RAIL_SERVICE = (
        "longDistanceInternationalRailService"
    )
    LONG_DISTANCE_RAIL_SERVICE = "longDistanceRailService"
    INTER_REGIONAL_EXPRESS_RAIL_SERVICE = "interRegionalExpressRailService"
    INTER_REGIONAL_RAIL_SERVICE = "interRegionalRailService"
    REGIONAL_EXPRESS_RAIL_SERVICE = "regionalExpressRailService"
    REGIONAL_RAIL_SERVICE = "regionalRailService"
    TOURIST_RAILWAY_SERVICE = "touristRailwayService"
    RAIL_SHUTTLE_SERVICE = "railShuttleService"
    SUBURBAN_RAIL_SERVICE = "suburbanRailService"
    SUBURBAN_NIGHT_RAIL_SERVICE = "suburbanNightRailService"
    SPECIAL_RAIL_SERVICE = "specialRailService"
    LORRY_TRANSPORT_RAIL_SERVICE = "lorryTransportRailService"
    VEHICLE_TRANSPORT_RAIL_SERVICE = "vehicleTransportRailService"
    VEHICLE_TUNNEL_TRANSPORT_RAIL_SERVICE = "vehicleTunnelTransportRailService"
    ADDITIONAL_RAIL_SERVICE = "additionalRailService"
    UNDEFINED_RAIL_SERVICE = "undefinedRailService"
    LONG_DISTANCE_TRAIN = "longDistanceTrain"
    SPECIAL_TRAIN_SERVICE = "specialTrainService"
    CROSS_COUNTRY_RAIL_SERVICE = "crossCountryRailService"
    VEHICLE_RAIL_TRANSPORT_SERVICE = "vehicleRailTransportService"
    ADDITIONAL_TRAIN_SERVICE = "additionalTrainService"
    ALL_RAIL_SERVICES = "allRailServices"
    UNDEFINED = "undefined"
    INTERBATIONAL = "interbational"
    PTI2_0 = "pti2_0"
    PTI2_1 = "pti2_1"
    PTI2_2 = "pti2_2"
    PTI2_3 = "pti2_3"
    PTI2_4 = "pti2_4"
    PTI2_5 = "pti2_5"
    PTI2_6 = "pti2_6"
    PTI2_7 = "pti2_7"
    PTI2_8 = "pti2_8"
    PTI2_9 = "pti2_9"
    PTI2_10 = "pti2_10"
    PTI2_11 = "pti2_11"
    PTI2_12 = "pti2_12"
    PTI2_13 = "pti2_13"
    PTI2_14 = "pti2_14"
    PTI2_15 = "pti2_15"
    PTI2_16 = "pti2_16"
    PTI2_17 = "pti2_17"
    PTI2_255 = "pti2_255"
    LOC13_0 = "loc13_0"
    LOC13_1 = "loc13_1"
    LOC13_2 = "loc13_2"
    LOC13_3 = "loc13_3"
    LOC13_4 = "loc13_4"
    LOC13_5 = "loc13_5"
    LOC13_6 = "loc13_6"
    LOC13_7 = "loc13_7"
    LOC13_8 = "loc13_8"
