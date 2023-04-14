from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class LuggageFacilityEnumeration(Enum):
    """
    Values for Luggage Facility: TPEG pti_table 23.
    """
    UNKNOWN = "unknown"
    PTI23_17 = "pti23_17"
    BIKE_CARRIAGE = "bikeCarriage"
    BAGGAGE_STORAGE = "baggageStorage"
    LEFT_LUGGAGE = "leftLuggage"
    PORTERAGE = "porterage"
    BAGGAGE_TROLLEYS = "baggageTrolleys"
