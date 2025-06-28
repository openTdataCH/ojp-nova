from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TaxiSubmodesOfTransportEnumeration(Enum):
    """Values for Taxi ModesOfTransport: TPEG pti_table_11.

    :cvar UNKNOWN: Submode of transport is not known to the source
        system.
    :cvar UNDEFINED: (SIRI 2.1) - see also 'undefinedTaxiService'.
    :cvar COMMUNAL_TAXI:
    :cvar CHARTER_TAXI: (SIRI 2.1)
    :cvar WATER_TAXI:
    :cvar RAIL_TAXI:
    :cvar BIKE_TAXI:
    :cvar BLACK_CAB:
    :cvar MINI_CAB:
    :cvar ALL_TAXI_SERVICES:
    :cvar UNDEFINED_TAXI_SERVICE: Submode of transport is not supported
        in this list.
    :cvar PTI11_0: DEPRECATED since SIRI 2.1
    :cvar PTI11_1: DEPRECATED since SIRI 2.1
    :cvar PTI11_2: DEPRECATED since SIRI 2.1
    :cvar PTI11_3: DEPRECATED since SIRI 2.1
    :cvar PTI11_4: DEPRECATED since SIRI 2.1
    :cvar PTI11_5: DEPRECATED since SIRI 2.1
    :cvar PTI11_6: DEPRECATED since SIRI 2.1
    :cvar PTI11_7: DEPRECATED since SIRI 2.1
    :cvar PTI11_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    COMMUNAL_TAXI = "communalTaxi"
    CHARTER_TAXI = "charterTaxi"
    WATER_TAXI = "waterTaxi"
    RAIL_TAXI = "railTaxi"
    BIKE_TAXI = "bikeTaxi"
    BLACK_CAB = "blackCab"
    MINI_CAB = "miniCab"
    ALL_TAXI_SERVICES = "allTaxiServices"
    UNDEFINED_TAXI_SERVICE = "undefinedTaxiService"
    PTI11_0 = "pti11_0"
    PTI11_1 = "pti11_1"
    PTI11_2 = "pti11_2"
    PTI11_3 = "pti11_3"
    PTI11_4 = "pti11_4"
    PTI11_5 = "pti11_5"
    PTI11_6 = "pti11_6"
    PTI11_7 = "pti11_7"
    PTI11_255 = "pti11_255"
