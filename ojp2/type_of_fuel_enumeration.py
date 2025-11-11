from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TypeOfFuelEnumeration(Enum):
    """Allowed values for TYPE OF FUEL.

    (since SIRI 2.1)
    """

    PETROL = "petrol"
    DIESEL = "diesel"
    NATURAL_GAS = "naturalGas"
    BIODIESEL = "biodiesel"
    ELECTRICITY = "electricity"
    HYDROGEN = "hydrogen"
    OTHER = "other"
    UNKNOWN = "unknown"
