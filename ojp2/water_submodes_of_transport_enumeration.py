from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class WaterSubmodesOfTransportEnumeration(Enum):
    """Values for Water ModesOfTransport: TPEG pti_table_07 and pts_table_107.

    :cvar UNKNOWN: TPEG Pts107_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: (SIRI 2.1) - see also 'undefinedWaterTransport'.
    :cvar INTERNATIONAL_CAR_FERRY: (SIRI 2.1) - see also
        'internationalCarFerryService'.
    :cvar NATIONAL_CAR_FERRY: (SIRI 2.1) - see also
        'nationalCarFerryService'.
    :cvar REGIONAL_CAR_FERRY: (SIRI 2.1) - see also
        'regionalCarFerryService'.
    :cvar LOCAL_CAR_FERRY: (SIRI 2.1) - see also 'localCarFerryService'.
    :cvar INTERNATIONAL_PASSENGER_FERRY:
    :cvar NATIONAL_PASSENGER_FERRY:
    :cvar REGIONAL_PASSENGER_FERRY:
    :cvar LOCAL_PASSENGER_FERRY:
    :cvar POST_BOAT:
    :cvar TRAIN_FERRY:
    :cvar ROAD_FERRY_LINK:
    :cvar AIRPORT_BOAT_LINK:
    :cvar HIGH_SPEED_VEHICLE_SERVICE:
    :cvar HIGH_SPEED_PASSENGER_SERVICE:
    :cvar SIGHTSEEING_SERVICE:
    :cvar SCHOOL_BOAT:
    :cvar CABLE_FERRY:
    :cvar RIVER_BUS:
    :cvar SCHEDULED_FERRY:
    :cvar SHUTTLE_FERRY_SERVICE:
    :cvar CANAL_BARGE: (SIRI 2.1)
    :cvar INTERNATIONAL_CAR_FERRY_SERVICE: TPEG Pts107_2
    :cvar NATIONAL_CAR_FERRY_SERVICE: TPEG Pts107_3
    :cvar REGIONAL_CAR_FERRY_SERVICE: TPEG Pts107_4
    :cvar LOCAL_CAR_FERRY_SERVICE: TPEG Pts107_5
    :cvar INTERNATIONAL_PASSENGER_FERRY_SERVICE: TPEG Pts107_6 (SIRI
        2.1) - see also 'internationalPassengerFerry'.
    :cvar NATIONAL_PASSENGER_FERRY_SERVICE: TPEG Pts107_7 (SIRI 2.1) -
        see also 'nationalPassengerFerry'.
    :cvar REGIONAL_PASSENGER_FERRY_SERVICE: TPEG Pts107_8 (SIRI 2.1) -
        see also 'regionalPassengerFerry'.
    :cvar LOCAL_PASSENGER_FERRY_SERVICE: TPEG Pts107_9 (SIRI 2.1) - see
        also 'localPassengerFerry'.
    :cvar POST_BOAT_SERVICE: TPEG Pts107_10 (SIRI 2.1) - see also
        'postBoat'.
    :cvar TRAIN_FERRY_SERVICE: TPEG Pts107_11 (SIRI 2.1) - see also
        'trainFerry'.
    :cvar ROAD_LINK_FERRY_SERVICE: TPEG Pts107_12 (SIRI 2.1) - see also
        'roadFerryLink'.
    :cvar AIRPORT_LINK_FERRY_SERVICE: TPEG Pts107_13 (SIRI 2.1) - see
        also 'airportBoatLink'.
    :cvar CAR_HIGH_SPEED_FERRY_SERVICE: TPEG Pts107_14 (SIRI 2.1) - see
        also 'highSpeedVehicleService'.
    :cvar PASSENGER_HIGH_SPEED_FERRY_SERVICE: TPEG Pts107_15 (SIRI 2.1)
        - see also 'highSpeedPassengerService'.
    :cvar SCHEDULED_BOAT_SERVICE: TPEG Pts107_16 (SIRI 2.1) - see also
        'scheduledFerry'.
    :cvar SCHEDULED_EXPRESS_BOAT_SERVICE: TPEG Pts107_17 (SIRI 2.1)
    :cvar ADDITIONAL_BOAT_SERVICE: TPEG Pts107_18 (SIRI 2.1)
    :cvar SIGHTSEEING_BOAT_SERVICE: TPEG Pts107_19 (SIRI 2.1) - see also
        'sightseeingService'.
    :cvar SCHOOL_BOAT_SERVICE: TPEG Pts107_20 (SIRI 2.1) - see also
        'schoolBoat'.
    :cvar RIVER_BUS_SERVICE: TPEG Pts107_21 (SIRI 2.1) - see also
        'riverBus'.
    :cvar SCHEDULED_FERRY_SERVICE: TPEG Pts107_22 (SIRI 2.1) - see also
        'scheduledFerry'.
    :cvar UNDEFINED_WATER_TRANSPORT_SERVICE: TPEG Pts107_255 (SIRI 2.1)
        - see also 'undefinedWaterTransport'.
    :cvar UNDEFINED_WATER_TRANSPORT: Submode of transport is not
        supported in this list.
    :cvar ALL_WATER_TRANSPORT_SERVICES:
    :cvar PTI7_0: DEPRECATED since SIRI 2.1
    :cvar PTI7_1: DEPRECATED since SIRI 2.1
    :cvar PTI7_2: DEPRECATED since SIRI 2.1
    :cvar PTI7_3: DEPRECATED since SIRI 2.1
    :cvar PTI7_4: DEPRECATED since SIRI 2.1
    :cvar PTI7_5: DEPRECATED since SIRI 2.1
    :cvar PTI7_6: DEPRECATED since SIRI 2.1
    :cvar PTI7_7: DEPRECATED since SIRI 2.1
    :cvar PTI7_8: DEPRECATED since SIRI 2.1
    :cvar PTI7_9: DEPRECATED since SIRI 2.1
    :cvar PTI7_10: DEPRECATED since SIRI 2.1
    :cvar PTI7_11: DEPRECATED since SIRI 2.1
    :cvar PTI7_12: DEPRECATED since SIRI 2.1
    :cvar PTI7_13: DEPRECATED since SIRI 2.1
    :cvar PTI7_14: DEPRECATED since SIRI 2.1
    :cvar PTI7_15: DEPRECATED since SIRI 2.1
    :cvar PTI7_16: DEPRECATED since SIRI 2.1
    :cvar PTI7_17: DEPRECATED since SIRI 2.1
    :cvar PTI7_18: DEPRECATED since SIRI 2.1
    :cvar PTI7_19: DEPRECATED since SIRI 2.1
    :cvar PTI7_20: DEPRECATED since SIRI 2.1
    :cvar PTI7_21: DEPRECATED since SIRI 2.1
    :cvar PTI7_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_CAR_FERRY = "internationalCarFerry"
    NATIONAL_CAR_FERRY = "nationalCarFerry"
    REGIONAL_CAR_FERRY = "regionalCarFerry"
    LOCAL_CAR_FERRY = "localCarFerry"
    INTERNATIONAL_PASSENGER_FERRY = "internationalPassengerFerry"
    NATIONAL_PASSENGER_FERRY = "nationalPassengerFerry"
    REGIONAL_PASSENGER_FERRY = "regionalPassengerFerry"
    LOCAL_PASSENGER_FERRY = "localPassengerFerry"
    POST_BOAT = "postBoat"
    TRAIN_FERRY = "trainFerry"
    ROAD_FERRY_LINK = "roadFerryLink"
    AIRPORT_BOAT_LINK = "airportBoatLink"
    HIGH_SPEED_VEHICLE_SERVICE = "highSpeedVehicleService"
    HIGH_SPEED_PASSENGER_SERVICE = "highSpeedPassengerService"
    SIGHTSEEING_SERVICE = "sightseeingService"
    SCHOOL_BOAT = "schoolBoat"
    CABLE_FERRY = "cableFerry"
    RIVER_BUS = "riverBus"
    SCHEDULED_FERRY = "scheduledFerry"
    SHUTTLE_FERRY_SERVICE = "shuttleFerryService"
    CANAL_BARGE = "canalBarge"
    INTERNATIONAL_CAR_FERRY_SERVICE = "internationalCarFerryService"
    NATIONAL_CAR_FERRY_SERVICE = "nationalCarFerryService"
    REGIONAL_CAR_FERRY_SERVICE = "regionalCarFerryService"
    LOCAL_CAR_FERRY_SERVICE = "localCarFerryService"
    INTERNATIONAL_PASSENGER_FERRY_SERVICE = (
        "internationalPassengerFerryService"
    )
    NATIONAL_PASSENGER_FERRY_SERVICE = "nationalPassengerFerryService"
    REGIONAL_PASSENGER_FERRY_SERVICE = "regionalPassengerFerryService"
    LOCAL_PASSENGER_FERRY_SERVICE = "localPassengerFerryService"
    POST_BOAT_SERVICE = "postBoatService"
    TRAIN_FERRY_SERVICE = "trainFerryService"
    ROAD_LINK_FERRY_SERVICE = "roadLinkFerryService"
    AIRPORT_LINK_FERRY_SERVICE = "airportLinkFerryService"
    CAR_HIGH_SPEED_FERRY_SERVICE = "carHighSpeedFerryService"
    PASSENGER_HIGH_SPEED_FERRY_SERVICE = "passengerHighSpeedFerryService"
    SCHEDULED_BOAT_SERVICE = "scheduledBoatService"
    SCHEDULED_EXPRESS_BOAT_SERVICE = "scheduledExpressBoatService"
    ADDITIONAL_BOAT_SERVICE = "additionalBoatService"
    SIGHTSEEING_BOAT_SERVICE = "sightseeingBoatService"
    SCHOOL_BOAT_SERVICE = "schoolBoatService"
    RIVER_BUS_SERVICE = "riverBusService"
    SCHEDULED_FERRY_SERVICE = "scheduledFerryService"
    UNDEFINED_WATER_TRANSPORT_SERVICE = "undefinedWaterTransportService"
    UNDEFINED_WATER_TRANSPORT = "undefinedWaterTransport"
    ALL_WATER_TRANSPORT_SERVICES = "allWaterTransportServices"
    PTI7_0 = "pti7_0"
    PTI7_1 = "pti7_1"
    PTI7_2 = "pti7_2"
    PTI7_3 = "pti7_3"
    PTI7_4 = "pti7_4"
    PTI7_5 = "pti7_5"
    PTI7_6 = "pti7_6"
    PTI7_7 = "pti7_7"
    PTI7_8 = "pti7_8"
    PTI7_9 = "pti7_9"
    PTI7_10 = "pti7_10"
    PTI7_11 = "pti7_11"
    PTI7_12 = "pti7_12"
    PTI7_13 = "pti7_13"
    PTI7_14 = "pti7_14"
    PTI7_15 = "pti7_15"
    PTI7_16 = "pti7_16"
    PTI7_17 = "pti7_17"
    PTI7_18 = "pti7_18"
    PTI7_19 = "pti7_19"
    PTI7_20 = "pti7_20"
    PTI7_21 = "pti7_21"
    PTI7_255 = "pti7_255"
