from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FacilityCategoryEnumeration(Enum):
    """
    Generic category of a facility.
    """

    UNKNOWN = "unknown"
    FIXED_EQUIPMENT = "fixedEquipment"
    MOBILE_EQUIPMENT = "mobileEquipment"
    SERVICE_PROVIDED_BY_INDIVIDUAL = "serviceProvidedByIndividual"
    SERVICE_FOR_PERSONAL_DEVICE = "serviceForPersonalDevice"
    RESERVED_AREA = "reservedArea"
    SITE = "site"
    SITE_COMPONENT = "siteComponent"
    PARKING_BAY = "parkingBay"
    VEHICLE = "vehicle"
