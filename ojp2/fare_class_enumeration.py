from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FareClassEnumeration(Enum):
    """Values for Fare Class Facility.

    (since SIRI 2.1)

    :cvar UNKNOWN: pti23_0
    :cvar FIRST_CLASS: pti23_6
    :cvar SECOND_CLASS: pti23_7
    :cvar THIRD_CLASS: pti23_8
    :cvar PREFERENTE:
    :cvar PREMIUM_CLASS: pti23_6_1
    :cvar BUSINESS_CLASS: Business Class - pti23_10
    :cvar STANDARD_CLASS: Standard class Add pti23_7
    :cvar TURISTA:
    :cvar ECONOMY_CLASS: pti23_9
    :cvar ANY:
    """

    UNKNOWN = "unknown"
    FIRST_CLASS = "firstClass"
    SECOND_CLASS = "secondClass "
    THIRD_CLASS = "thirdClass"
    PREFERENTE = "preferente"
    PREMIUM_CLASS = "premiumClass"
    BUSINESS_CLASS = "businessClass"
    STANDARD_CLASS = "standardClass"
    TURISTA = "turista"
    ECONOMY_CLASS = "economyClass"
    ANY = "any"
