from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FacilityCategoryEnumeration(Enum):
    """
    Generic catégory of a facility.
    """
    UNKNOWN = "unknown"
    FIXED_EQUIPMENT = "fixedEquipment"
    SERVICE_PROVIDED_BY_INDIVIDUAL = "serviceProvidedByIndividual"
    SERVICE_FOR_PERSONAL_DEVICE = "serviceForPersonalDevice"
    RESERVED_AREA = "reservedArea"
