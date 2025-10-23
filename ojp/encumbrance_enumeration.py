from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class EncumbranceEnumeration(Enum):
    """
    Enumeration of specific encumbrances USER NEEDs.
    """
    LUGGAGE_ENCUMBERED = "luggageEncumbered"
    PUSHCHAIR = "pushchair"
    BAGGAGE_TROLLEY = "baggageTrolley"
    OVERSIZE_BAGGAGE = "oversizeBaggage"
    GUIDE_DOG = "guideDog"
    OTHER_ANIMAL = "otherAnimal"
    OTHER_ENCUMBRANCE = "otherEncumbrance"
