from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleModesOfTransportEnumeration(Enum):
    """Values for ModesOfTransport : TPEG Pti01 and Pts001 "ModeOfTransport".

    :cvar AIR:
    :cvar BUS:
    :cvar COACH:
    :cvar FERRY: (SIRI 2.1)
    :cvar METRO:
    :cvar RAIL:
    :cvar TROLLEY_BUS:
    :cvar TRAM:
    :cvar WATER:
    :cvar CABLEWAY: (SIRI 2.1)
    :cvar FUNICULAR:
    :cvar LIFT:
    :cvar SNOW_AND_ICE: (SIRI 2.1)
    :cvar OTHER: Placeholder value if mode of transport is different
        from all other enumerations in this list (SIRI 2.1) - same
        meaning as 'undefinedModeOfTransport'.
    :cvar UNKNOWN: TPEG Pts1_0 - mode of transport is not known to the
        source system.
    :cvar AIR_SERVICE: TPEG Pts1_1 - use 'air' instead.
    :cvar GONDOLA_CABLE_CAR_SERVICE: TPEG Pts1_2 (SIRI 2.1) - see also
        'cableway'.
    :cvar CHAIRLIFT_SERVICE: TPEG Pts1_3 (SIRI 2.1)
    :cvar ELEVATOR_SERVICE: TPEG Pts1_4 (SIRI 2.1) - use 'lift' instead.
    :cvar RAILWAY_SERVICE: TPEG Pts1_5 - use 'rail' instead.
    :cvar URBAN_RAILWAY_SERVICE: TPEG Pts1_6 - see also 'urbanRail'.
    :cvar LIGHT_RAILWAY_SERVICE: TPEG Pts1_7 (SIRI 2.1)
    :cvar RACK_RAIL_SERVICE: TPEG Pts1_8 (SIRI 2.1)
    :cvar FUNICULAR_SERVICE: TPEG Pts1_9 - use 'funicular' instead.
    :cvar BUS_SERVICE: TPEG Pts1_10 - use 'bus' instead.
    :cvar TROLLEYBUS_SERVICE: TPEG Pts1_11 (SIRI 2.1) - use 'trolleyBus'
        instead.
    :cvar COACH_SERVICE: TPEG Pts1_12 - use 'coach' instead.
    :cvar TAXI_SERVICE: TPEG Pts1_13 - use 'taxi' instead.
    :cvar RENTAL_VEHICLE: TPEG Pts1_14 (SIRI 2.1)
    :cvar WATER_TRANSPORT_SERVICE: TPEG Pts1_15 - use 'water' instead.
    :cvar CABLE_DRAWN_BOAT_SERVICE: TPEG Pts1_16 (SIRI 2.1)
    :cvar UNDEFINED_MODE_OF_TRANSPORT: TPEG Pts1_255 (SIRI 2.1) - mode
        of transport is not supported in this list.
    :cvar SUBURBAN_RAIL:
    :cvar SUBURBAN_RAILWAY_SERVICE: See also 'suburbanRail'.
    :cvar URBAN_RAIL:
    :cvar UNDERGROUND:
    :cvar UNDERGROUND_SERVICE: See also 'underground'.
    :cvar METRO_SERVICE: Use 'metro' instead.
    :cvar TROLLEY_BUS_SERVICE_1: Use 'trolleyBus' instead.
    :cvar TRAM_SERVICE: Use 'tram' instead.
    :cvar WATER_TRANSPORT: Use 'water' instead.
    :cvar FERRY_SERVICE: Use 'ferry' instead.
    :cvar TELECABIN: See also 'cableway'.
    :cvar TELECABIN_SERVICE: See also 'telecabin'.
    :cvar TAXI:
    :cvar SELF_DRIVE:
    :cvar ALL:
    :cvar ALL_SERVICES: See also 'all'.
    :cvar ALL_SERVICES_EXCEPT:
    :cvar PTI1_0: DEPRECATED since SIRI 2.1
    :cvar PTI1_1: DEPRECATED since SIRI 2.1
    :cvar PTI1_2: DEPRECATED since SIRI 2.1
    :cvar PTI1_3: DEPRECATED since SIRI 2.1
    :cvar PTI1_4: DEPRECATED since SIRI 2.1
    :cvar PTI1_5: DEPRECATED since SIRI 2.1
    :cvar PTI1_6: DEPRECATED since SIRI 2.1
    :cvar PTI1_7: DEPRECATED since SIRI 2.1
    :cvar PTI1_8: DEPRECATED since SIRI 2.1
    :cvar PTI1_9: DEPRECATED since SIRI 2.1
    :cvar PTI1_10: DEPRECATED since SIRI 2.1
    :cvar PTI1_11: DEPRECATED since SIRI 2.1
    :cvar PTI1_12: DEPRECATED since SIRI 2.1
    :cvar PTI1_13: DEPRECATED since SIRI 2.1
    :cvar PTI1_14: DEPRECATED since SIRI 2.1
    :cvar PTI1_15: DEPRECATED since SIRI 2.1
    :cvar PTI1_16: DEPRECATED since SIRI 2.1
    :cvar PTI1_17: DEPRECATED since SIRI 2.1
    :cvar PTI1_18: DEPRECATED since SIRI 2.1
    """

    AIR = "air"
    BUS = "bus"
    COACH = "coach"
    FERRY = "ferry"
    METRO = "metro"
    RAIL = "rail"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    LIFT = "lift"
    SNOW_AND_ICE = "snowAndIce"
    OTHER = "other"
    UNKNOWN = "unknown"
    AIR_SERVICE = "airService"
    GONDOLA_CABLE_CAR_SERVICE = "gondolaCableCarService"
    CHAIRLIFT_SERVICE = "chairliftService"
    ELEVATOR_SERVICE = "elevatorService"
    RAILWAY_SERVICE = "railwayService"
    URBAN_RAILWAY_SERVICE = "urbanRailwayService"
    LIGHT_RAILWAY_SERVICE = "lightRailwayService"
    RACK_RAIL_SERVICE = "rackRailService"
    FUNICULAR_SERVICE = "funicularService"
    BUS_SERVICE = "busService"
    TROLLEYBUS_SERVICE = "trolleybusService"
    COACH_SERVICE = "coachService"
    TAXI_SERVICE = "taxiService"
    RENTAL_VEHICLE = "rentalVehicle"
    WATER_TRANSPORT_SERVICE = "waterTransportService"
    CABLE_DRAWN_BOAT_SERVICE = "cableDrawnBoatService"
    UNDEFINED_MODE_OF_TRANSPORT = "undefinedModeOfTransport"
    SUBURBAN_RAIL = "suburbanRail"
    SUBURBAN_RAILWAY_SERVICE = "suburbanRailwayService"
    URBAN_RAIL = "urbanRail"
    UNDERGROUND = "underground"
    UNDERGROUND_SERVICE = "undergroundService"
    METRO_SERVICE = "metroService"
    TROLLEY_BUS_SERVICE_1 = "trolleyBusService"
    TRAM_SERVICE = "tramService"
    WATER_TRANSPORT = "waterTransport"
    FERRY_SERVICE = "ferryService"
    TELECABIN = "telecabin"
    TELECABIN_SERVICE = "telecabinService"
    TAXI = "taxi"
    SELF_DRIVE = "selfDrive"
    ALL = "all"
    ALL_SERVICES = "allServices"
    ALL_SERVICES_EXCEPT = "allServicesExcept"
    PTI1_0 = "pti1_0"
    PTI1_1 = "pti1_1"
    PTI1_2 = "pti1_2"
    PTI1_3 = "pti1_3"
    PTI1_4 = "pti1_4"
    PTI1_5 = "pti1_5"
    PTI1_6 = "pti1_6"
    PTI1_7 = "pti1_7"
    PTI1_8 = "pti1_8"
    PTI1_9 = "pti1_9"
    PTI1_10 = "pti1_10"
    PTI1_11 = "pti1_11"
    PTI1_12 = "pti1_12"
    PTI1_13 = "pti1_13"
    PTI1_14 = "pti1_14"
    PTI1_15 = "pti1_15"
    PTI1_16 = "pti1_16"
    PTI1_17 = "pti1_17"
    PTI1_18 = "pti1_18"
