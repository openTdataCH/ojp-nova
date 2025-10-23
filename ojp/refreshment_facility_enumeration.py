from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RefreshmentFacilityEnumeration(Enum):
    """
    Values for Refreshment Facility: TPEG pti_table 23.
    """
    UNKNOWN = "unknown"
    PTI23_1 = "pti23_1"
    RESTAURANT_SERVICE = "restaurantService"
    PTI23_2 = "pti23_2"
    SNACKS_SERVICE = "snacksService"
    PTI23 = "pti23"
    TROLLEY = "trolley"
    PTI23_18 = "pti23_18"
    BAR = "bar"
    PTI23_19 = "pti23_19"
    FOOD_NOT_AVAILABLE = "foodNotAvailable"
    PTI23_20 = "pti23_20"
    BEVERAGES_NOT_AVAILABLE = "beveragesNotAvailable"
    PTI23_26 = "pti23_26"
    BISTRO = "bistro"
    FOOD_VENDING_MACHINE = "foodVendingMachine"
    BEVERAGE_VENDING_MACHINE = "beverageVendingMachine"
