from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TaxiSubmodesOfTransportEnumeration(Enum):
    """
    Values for Taxi ModesOfTransport: TPEG pti_table_11.
    """
    PTI11_0 = "pti11_0"
    UNKNOWN = "unknown"
    PTI11_1 = "pti11_1"
    COMMUNAL_TAXI = "communalTaxi"
    PTI11_2 = "pti11_2"
    WATER_TAXI = "waterTaxi"
    PTI11_3 = "pti11_3"
    RAIL_TAXI = "railTaxi"
    PTI11_4 = "pti11_4"
    BIKE_TAXI = "bikeTaxi"
    PTI11_5 = "pti11_5"
    BLACK_CAB = "blackCab"
    PTI11_6 = "pti11_6"
    MINI_CAB = "miniCab"
    PTI11_7 = "pti11_7"
    ALL_TAXI_SERVICES = "allTaxiServices"
    PTI11_255 = "pti11_255"
    UNDEFINED_TAXI_SERVICE = "undefinedTaxiService"
