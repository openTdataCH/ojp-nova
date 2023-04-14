from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TypeOfFareClassEnumeration(Enum):
    """
    classes of travel available on a particular service which will affect the
    price to be paid.
    """
    ALL = "all"
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    BUSINESS = "business"
    ECONOMY = "economy"
