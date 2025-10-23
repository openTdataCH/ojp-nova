from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleModesOfTransportEnumeration(Enum):
    """Values for ModesOfTransport : TPEG pti_table 01.

    :cvar PTI1_0:
    :cvar UNKNOWN:
    :cvar PTI1_1:
    :cvar RAILWAY_SERVICE: See pti2_x.
    :cvar RAIL:
    :cvar PTI1_2:
    :cvar COACH_SERVICE: See pti3_x.
    :cvar COACH:
    :cvar PTI1_3:
    :cvar SUBURBAN_RAILWAY_SERVICE:
    :cvar SUBURBAN_RAIL:
    :cvar PTI1_4:
    :cvar URBAN_RAILWAY_SERVICE: See pti4_x.
    :cvar URBAN_RAIL:
    :cvar PTI1_5:
    :cvar METRO_SERVICE:
    :cvar METRO:
    :cvar PTI1_6:
    :cvar UNDERGROUND_SERVICE:
    :cvar UNDERGROUND:
    :cvar PTI1_7:
    :cvar BUS_SERVICE: See pti5_x.
    :cvar BUS:
    :cvar PTI1_8:
    :cvar TROLLEY_BUS_SERVICE:
    :cvar TROLLEY_BUS:
    :cvar PTI1_9:
    :cvar TRAM_SERVICE: See pti6_x.
    :cvar TRAM:
    :cvar PTI1_10:
    :cvar WATER_TRANSPORT_SERVICE: See pti7_x.
    :cvar WATER_TRANSPORT:
    :cvar PTI1_11:
    :cvar AIR_SERVICE: See pti8_x.
    :cvar AIR:
    :cvar PTI1_12:
    :cvar FERRY_SERVICE:
    :cvar WATER:
    :cvar PTI1_13:
    :cvar TELECABIN_SERVICE: See pti9_x.
    :cvar TELECABIN:
    :cvar PTI1_14:
    :cvar FUNICULAR_SERVICE: See pti10_x.
    :cvar FUNICULAR:
    :cvar PTI1_15:
    :cvar TAXI_SERVICE: pti11_x.
    :cvar TAXI:
    :cvar PTI1_16:
    :cvar SELF_DRIVE: See pti12_x.
    :cvar PTI1_17:
    :cvar ALL_SERVICES:
    :cvar ALL:
    :cvar PTI1_18:
    :cvar ALL_SERVICES_EXCEPT:
    """
    PTI1_0 = "pti1_0"
    UNKNOWN = "unknown"
    PTI1_1 = "pti1_1"
    RAILWAY_SERVICE = "railwayService"
    RAIL = "rail"
    PTI1_2 = "pti1_2"
    COACH_SERVICE = "coachService"
    COACH = "coach"
    PTI1_3 = "pti1_3"
    SUBURBAN_RAILWAY_SERVICE = "suburbanRailwayService"
    SUBURBAN_RAIL = "suburbanRail"
    PTI1_4 = "pti1_4"
    URBAN_RAILWAY_SERVICE = "urbanRailwayService"
    URBAN_RAIL = "urbanRail"
    PTI1_5 = "pti1_5"
    METRO_SERVICE = "metroService"
    METRO = "metro"
    PTI1_6 = "pti1_6"
    UNDERGROUND_SERVICE = "undergroundService"
    UNDERGROUND = "underground"
    PTI1_7 = "pti1_7"
    BUS_SERVICE = "busService"
    BUS = "bus"
    PTI1_8 = "pti1_8"
    TROLLEY_BUS_SERVICE = "trolleyBusService"
    TROLLEY_BUS = "trolleyBus"
    PTI1_9 = "pti1_9"
    TRAM_SERVICE = "tramService"
    TRAM = "tram"
    PTI1_10 = "pti1_10"
    WATER_TRANSPORT_SERVICE = "waterTransportService"
    WATER_TRANSPORT = "waterTransport"
    PTI1_11 = "pti1_11"
    AIR_SERVICE = "airService"
    AIR = "air"
    PTI1_12 = "pti1_12"
    FERRY_SERVICE = "ferryService"
    WATER = "water"
    PTI1_13 = "pti1_13"
    TELECABIN_SERVICE = "telecabinService"
    TELECABIN = "telecabin"
    PTI1_14 = "pti1_14"
    FUNICULAR_SERVICE = "funicularService"
    FUNICULAR = "funicular"
    PTI1_15 = "pti1_15"
    TAXI_SERVICE = "taxiService"
    TAXI = "taxi"
    PTI1_16 = "pti1_16"
    SELF_DRIVE = "selfDrive"
    PTI1_17 = "pti1_17"
    ALL_SERVICES = "allServices"
    ALL = "all"
    PTI1_18 = "pti1_18"
    ALL_SERVICES_EXCEPT = "allServicesExcept"
