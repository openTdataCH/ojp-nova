from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AirSubmodesOfTransportEnumeration(Enum):
    """Values for Air ModesOfTransport: TPEG pti_table_08 and pts_table_108.

    :cvar UNKNOWN: TPEG Pts108_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: (SIRI 2.1) - see also 'undefinedAircraftService'.
    :cvar INTERNATIONAL_FLIGHT:
    :cvar DOMESTIC_FLIGHT:
    :cvar INTERCONTINENTAL_FLIGHT:
    :cvar DOMESTIC_SCHEDULED_FLIGHT:
    :cvar SHUTTLE_FLIGHT:
    :cvar INTERCONTINENTAL_CHARTER_FLIGHT:
    :cvar INTERNATIONAL_CHARTER_FLIGHT:
    :cvar ROUND_TRIP_CHARTER_FLIGHT:
    :cvar SIGHTSEEING_FLIGHT:
    :cvar HELICOPTER_SERVICE:
    :cvar DOMESTIC_CHARTER_FLIGHT:
    :cvar SCHENGEN_AREA_FLIGHT:
    :cvar AIRSHIP_SERVICE: TPEG Pts108_13
    :cvar SHORT_HAUL_INTERNATIONAL_FLIGHT:
    :cvar INTERNATIONAL_AIR_SERVICE: TPEG Pts108_1 (SIRI 2.1) - see also
        'internationalFlight'.
    :cvar NATIONAL_AIR_SERVICE: TPEG Pts108_2 (SIRI 2.1) - see also
        'domesticFlight'.
    :cvar INTERCONTINENTAL_AIR_SERVICE: TPEG Pts108_3 (SIRI 2.1) - see
        also 'intercontinentalFlight'.
    :cvar NATIONAL_SCHEDULED_AIR_SERVICE: TPEG Pts108_4 (SIRI 2.1) - see
        also 'domesticScheduledFlight'.
    :cvar SHUTTLE_AIR_SERVICE: TPEG Pts108_5 (SIRI 2.1) - see also
        'shuttleFlight'.
    :cvar INTERCONTINENTAL_AIR_CHARTER_SERVICE: TPEG Pts108_6 (SIRI 2.1)
        - see also 'intercontinentalCharterFlight'.
    :cvar INTERNATIONAL_AIR_CHARTER_SERVICE: TPEG Pts108_7 (SIRI 2.1) -
        see also 'intercontinentalCharterFlight'.
    :cvar ROUND_TRIP_AIR_CHARTER_SERVICE: TPEG Pts108_8 (SIRI 2.1) - see
        also 'roundTripCharterFlight'.
    :cvar SIGHTSEEING_AIR_SERVICE: TPEG Pts108_9 (SIRI 2.1) - see also
        'sightseeingFlight'.
    :cvar HELICOPTER_AIR_SERVICE: TPEG Pts108_10 (SIRI 2.1) - see also
        'helicopterService'.
    :cvar DOMESTIC_AIR_CHARTER_SERVICE: TPEG Pts108_11 (SIRI 2.1) - see
        also 'domesticCharterFlight'.
    :cvar SCHENGEN_AREA_AIR_SERVICE: TPEG Pts108_12 (SIRI 2.1) - see
        also 'SchengenAreaFlight'.
    :cvar ON_DEMAND_SERVICE: TPEG Pts108_14 (SIRI 2.1)
    :cvar UNDEFINED_AIR_SERVICE: TPEG Pts108_15 (SIRI 2.1) - see also
        'undefinedAircraftService'.
    :cvar UNDEFINED_AIRCRAFT_SERVICE: Submode of transport is not
        supported in this list.
    :cvar ALL_AIR_SERVICES:
    :cvar PTI8_0: DEPRECATED since SIRI 2.1
    :cvar PTI8_1: DEPRECATED since SIRI 2.1
    :cvar PTI8_2: DEPRECATED since SIRI 2.1
    :cvar PTI8_3: DEPRECATED since SIRI 2.1
    :cvar PTI8_4: DEPRECATED since SIRI 2.1
    :cvar PTI8_5: DEPRECATED since SIRI 2.1
    :cvar PTI8_6: DEPRECATED since SIRI 2.1
    :cvar PTI8_7: DEPRECATED since SIRI 2.1
    :cvar PTI8_8: DEPRECATED since SIRI 2.1
    :cvar PTI8_9: DEPRECATED since SIRI 2.1
    :cvar PTI8_10: DEPRECATED since SIRI 2.1
    :cvar PTI8_11: DEPRECATED since SIRI 2.1
    :cvar PTI8_12: DEPRECATED since SIRI 2.1
    :cvar PTI8_13: DEPRECATED since SIRI 2.1
    :cvar PTI8_14: DEPRECATED since SIRI 2.1
    :cvar PTI8_255: DEPRECATED since SIRI 2.1
    :cvar LOC15_0: DEPRECATED since SIRI 2.1
    :cvar LOC15_1: DEPRECATED since SIRI 2.1
    :cvar LOC15_2: DEPRECATED since SIRI 2.1
    :cvar LOC14_3: DEPRECATED since SIRI 2.1
    :cvar LOC15_4: DEPRECATED since SIRI 2.1
    :cvar LOC15_5: DEPRECATED since SIRI 2.1
    :cvar LOC15_6: DEPRECATED since SIRI 2.1
    :cvar LOC15_7: DEPRECATED since SIRI 2.1
    :cvar LOC15_8: DEPRECATED since SIRI 2.1
    :cvar LOC15_9: DEPRECATED since SIRI 2.1
    :cvar LOC15_10: DEPRECATED since SIRI 2.1
    :cvar LOC15_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_FLIGHT = "internationalFlight"
    DOMESTIC_FLIGHT = "domesticFlight"
    INTERCONTINENTAL_FLIGHT = "intercontinentalFlight"
    DOMESTIC_SCHEDULED_FLIGHT = "domesticScheduledFlight"
    SHUTTLE_FLIGHT = "shuttleFlight"
    INTERCONTINENTAL_CHARTER_FLIGHT = "intercontinentalCharterFlight"
    INTERNATIONAL_CHARTER_FLIGHT = "internationalCharterFlight"
    ROUND_TRIP_CHARTER_FLIGHT = "roundTripCharterFlight"
    SIGHTSEEING_FLIGHT = "sightseeingFlight"
    HELICOPTER_SERVICE = "helicopterService"
    DOMESTIC_CHARTER_FLIGHT = "domesticCharterFlight"
    SCHENGEN_AREA_FLIGHT = "SchengenAreaFlight"
    AIRSHIP_SERVICE = "airshipService"
    SHORT_HAUL_INTERNATIONAL_FLIGHT = "shortHaulInternationalFlight"
    INTERNATIONAL_AIR_SERVICE = "internationalAirService"
    NATIONAL_AIR_SERVICE = "nationalAirService"
    INTERCONTINENTAL_AIR_SERVICE = "intercontinentalAirService"
    NATIONAL_SCHEDULED_AIR_SERVICE = "nationalScheduledAirService"
    SHUTTLE_AIR_SERVICE = "shuttleAirService"
    INTERCONTINENTAL_AIR_CHARTER_SERVICE = "intercontinentalAirCharterService"
    INTERNATIONAL_AIR_CHARTER_SERVICE = "internationalAirCharterService"
    ROUND_TRIP_AIR_CHARTER_SERVICE = "roundTripAirCharterService"
    SIGHTSEEING_AIR_SERVICE = "sightseeingAirService"
    HELICOPTER_AIR_SERVICE = "helicopterAirService"
    DOMESTIC_AIR_CHARTER_SERVICE = "domesticAirCharterService"
    SCHENGEN_AREA_AIR_SERVICE = "SchengenAreaAirService"
    ON_DEMAND_SERVICE = "onDemandService"
    UNDEFINED_AIR_SERVICE = "undefinedAirService"
    UNDEFINED_AIRCRAFT_SERVICE = "undefinedAircraftService"
    ALL_AIR_SERVICES = "allAirServices"
    PTI8_0 = "pti8_0"
    PTI8_1 = "pti8_1"
    PTI8_2 = "pti8_2"
    PTI8_3 = "pti8_3"
    PTI8_4 = "pti8_4"
    PTI8_5 = "pti8_5"
    PTI8_6 = "pti8_6"
    PTI8_7 = "pti8_7"
    PTI8_8 = "pti8_8"
    PTI8_9 = "pti8_9"
    PTI8_10 = "pti8_10"
    PTI8_11 = "pti8_11"
    PTI8_12 = "pti8_12"
    PTI8_13 = "pti8_13"
    PTI8_14 = "pti8_14"
    PTI8_255 = "pti8_255"
    LOC15_0 = "loc15_0"
    LOC15_1 = "loc15_1"
    LOC15_2 = "loc15_2"
    LOC14_3 = "loc14_3"
    LOC15_4 = "loc15_4"
    LOC15_5 = "loc15_5"
    LOC15_6 = "loc15_6"
    LOC15_7 = "loc15_7"
    LOC15_8 = "loc15_8"
    LOC15_9 = "loc15_9"
    LOC15_10 = "loc15_10"
    LOC15_255 = "loc15_255"
