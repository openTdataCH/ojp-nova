from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class BusSubmodesOfTransportEnumeration(Enum):
    """Values for Bus ModesOfTransport: TPEG pti_table_05, pts_table_105 and loc_table_10.

    :cvar UNKNOWN: TPEG Pts105_0 - submode of transport is not known to
        the source system.
    :cvar UNDEFINED: Submode of transport is not supported in this list.
    :cvar LOCAL_BUS: (SIRI 2.1) - see also 'localBusService'.
    :cvar REGIONAL_BUS:
    :cvar EXPRESS_BUS:
    :cvar NIGHT_BUS:
    :cvar POST_BUS:
    :cvar SPECIAL_NEEDS_BUS:
    :cvar MOBILITY_BUS:
    :cvar MOBILITY_BUS_FOR_REGISTERED_DISABLED:
    :cvar SIGHTSEEING_BUS:
    :cvar SHUTTLE_BUS:
    :cvar HIGH_FREQUENCY_BUS: (SIRI 2.1)
    :cvar DEDICATED_LANE_BUS: (SIRI 2.1)
    :cvar SCHOOL_BUS:
    :cvar SCHOOL_AND_PUBLIC_SERVICE_BUS:
    :cvar RAIL_REPLACEMENT_BUS:
    :cvar DEMAND_AND_RESPONSE_BUS:
    :cvar AIRPORT_LINK_BUS:
    :cvar REGIONAL_BUS_SERVICE: TPEG Pts105_1 (SIRI 2.1) - see also
        'regionalBus'.
    :cvar ADDITIONAL_BUS_SERVICE: TPEG Pts105_2 (SIRI 2.1)
    :cvar EXPRESS_BUS_SERVICE: TPEG Pts105_3 (SIRI 2.1) - see also
        'expressBus'.
    :cvar STOPPING_BUS_SERVICE: TPEG Pts105_4 (SIRI 2.1)
    :cvar LOCAL_BUS_SERVICE: TPEG Pts105_5 (SIRI 2.1)
    :cvar NIGHT_BUS_SERVICE: TPEG Pts105_6 (SIRI 2.1) - see also
        'nightBus'.
    :cvar POST_BUS_SERVICE: TPEG Pts105_7 (SIRI 2.1) - see also
        'postBus'.
    :cvar SPECIAL_NEEDS_BUS_SERVICE: TPEG Pts105_8 (SIRI 2.1) - see also
        'specialNeedsBus'.
    :cvar MOBILITY_BUS_SERVICE: TPEG Pts105_9 (SIRI 2.1) - see also
        'mobilityBus'.
    :cvar MOBILITY_BUS_FOR_REGISTERED_DISABLED_SERVICE: TPEG Pts105_10
        (SIRI 2.1) - see also 'mobilityBusForRegisteredDisabled'.
    :cvar SIGHTSEEING_BUS_SERVICE: TPEG Pts105_11 (SIRI 2.1) - see also
        'sightseeingBus'.
    :cvar SHUTTLE_BUS_SERVICE: TPEG Pts105_12 (SIRI 2.1) - see also
        'shuttleBus'.
    :cvar SCHOOL_BUS_SERVICE: TPEG Pts105_13 (SIRI 2.1) - see also
        'schoolBus'.
    :cvar SCHOOL_AND_PUBLIC_SERVICE_BUS_SERVICE: TPEG Pts105_14 (SIRI
        2.1) - see also 'schoolAndPublicServiceBus'.
    :cvar RAIL_REPLACEMENT_BUS_SERVICE: TPEG Pts105_15 (SIRI 2.1) - see
        also 'railReplacementBus'.
    :cvar DEMAND_AND_RESPONSE_BUS_SERVICE: TPEG Pts105_16 (SIRI 2.1) -
        see also 'demandAndResponseBus'.
    :cvar UNDEFINED_BUS_SERVICE: TPEG Pts105_255 (SIRI 2.1) - see also
        'undefined'.
    :cvar BUS:
    :cvar ALL_BUS_SERVICES:
    :cvar PTI5_0: DEPRECATED since SIRI 2.1
    :cvar PTI5_1: DEPRECATED since SIRI 2.1
    :cvar PTI5_2: DEPRECATED since SIRI 2.1
    :cvar PTI5_3: DEPRECATED since SIRI 2.1
    :cvar PTI5_4: DEPRECATED since SIRI 2.1
    :cvar PTI5_5: DEPRECATED since SIRI 2.1
    :cvar PTI5_6: DEPRECATED since SIRI 2.1
    :cvar PTI5_7: DEPRECATED since SIRI 2.1
    :cvar PTI5_8: DEPRECATED since SIRI 2.1
    :cvar PTI5_9: DEPRECATED since SIRI 2.1
    :cvar PTI5_10: DEPRECATED since SIRI 2.1
    :cvar PTI5_11: DEPRECATED since SIRI 2.1
    :cvar PTI5_12: DEPRECATED since SIRI 2.1
    :cvar PTI5_13: DEPRECATED since SIRI 2.1
    :cvar PTI5_14: DEPRECATED since SIRI 2.1
    :cvar PTI5_15: DEPRECATED since SIRI 2.1
    :cvar PTI5_16: DEPRECATED since SIRI 2.1
    :cvar PTI5_255: DEPRECATED since SIRI 2.1
    :cvar LOC_10: DEPRECATED since SIRI 2.1
    :cvar LOC10_0: DEPRECATED since SIRI 2.1
    :cvar LOC10_1: DEPRECATED since SIRI 2.1
    :cvar LOC10_2: DEPRECATED since SIRI 2.1
    :cvar LOC10_4: DEPRECATED since SIRI 2.1
    :cvar LOC10_5: DEPRECATED since SIRI 2.1
    :cvar LOC10_6: DEPRECATED since SIRI 2.1
    :cvar LOC10_7: DEPRECATED since SIRI 2.1
    :cvar LOC10_8: DEPRECATED since SIRI 2.1
    :cvar LOC10_9: DEPRECATED since SIRI 2.1
    :cvar LOC10_13: DEPRECATED since SIRI 2.1
    :cvar LOC10_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    LOCAL_BUS = "localBus"
    REGIONAL_BUS = "regionalBus"
    EXPRESS_BUS = "expressBus"
    NIGHT_BUS = "nightBus"
    POST_BUS = "postBus"
    SPECIAL_NEEDS_BUS = "specialNeedsBus"
    MOBILITY_BUS = "mobilityBus"
    MOBILITY_BUS_FOR_REGISTERED_DISABLED = "mobilityBusForRegisteredDisabled"
    SIGHTSEEING_BUS = "sightseeingBus"
    SHUTTLE_BUS = "shuttleBus"
    HIGH_FREQUENCY_BUS = "highFrequencyBus"
    DEDICATED_LANE_BUS = "dedicatedLaneBus"
    SCHOOL_BUS = "schoolBus"
    SCHOOL_AND_PUBLIC_SERVICE_BUS = "schoolAndPublicServiceBus"
    RAIL_REPLACEMENT_BUS = "railReplacementBus"
    DEMAND_AND_RESPONSE_BUS = "demandAndResponseBus"
    AIRPORT_LINK_BUS = "airportLinkBus"
    REGIONAL_BUS_SERVICE = "regionalBusService"
    ADDITIONAL_BUS_SERVICE = "additionalBusService"
    EXPRESS_BUS_SERVICE = "expressBusService"
    STOPPING_BUS_SERVICE = "stoppingBusService"
    LOCAL_BUS_SERVICE = "localBusService"
    NIGHT_BUS_SERVICE = "nightBusService"
    POST_BUS_SERVICE = "postBusService"
    SPECIAL_NEEDS_BUS_SERVICE = "specialNeedsBusService"
    MOBILITY_BUS_SERVICE = "mobilityBusService"
    MOBILITY_BUS_FOR_REGISTERED_DISABLED_SERVICE = (
        "mobilityBusForRegisteredDisabledService"
    )
    SIGHTSEEING_BUS_SERVICE = "sightseeingBusService"
    SHUTTLE_BUS_SERVICE = "shuttleBusService"
    SCHOOL_BUS_SERVICE = "schoolBusService"
    SCHOOL_AND_PUBLIC_SERVICE_BUS_SERVICE = "schoolAndPublicServiceBusService"
    RAIL_REPLACEMENT_BUS_SERVICE = "railReplacementBusService"
    DEMAND_AND_RESPONSE_BUS_SERVICE = "demandAndResponseBusService"
    UNDEFINED_BUS_SERVICE = "undefinedBusService"
    BUS = "bus"
    ALL_BUS_SERVICES = "allBusServices"
    PTI5_0 = "pti5_0"
    PTI5_1 = "pti5_1"
    PTI5_2 = "pti5_2"
    PTI5_3 = "pti5_3"
    PTI5_4 = "pti5_4"
    PTI5_5 = "pti5_5"
    PTI5_6 = "pti5_6"
    PTI5_7 = "pti5_7"
    PTI5_8 = "pti5_8"
    PTI5_9 = "pti5_9"
    PTI5_10 = "pti5_10"
    PTI5_11 = "pti5_11"
    PTI5_12 = "pti5_12"
    PTI5_13 = "pti5_13"
    PTI5_14 = "pti5_14"
    PTI5_15 = "pti5_15"
    PTI5_16 = "pti5_16"
    PTI5_255 = "pti5_255"
    LOC_10 = "loc_10"
    LOC10_0 = "loc10_0"
    LOC10_1 = "loc10_1"
    LOC10_2 = "loc10_2"
    LOC10_4 = "loc10_4"
    LOC10_5 = "loc10_5"
    LOC10_6 = "loc10_6"
    LOC10_7 = "loc10_7"
    LOC10_8 = "loc10_8"
    LOC10_9 = "loc10_9"
    LOC10_13 = "loc10_13"
    LOC10_255 = "loc10_255"
