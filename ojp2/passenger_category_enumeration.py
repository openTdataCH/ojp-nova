from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PassengerCategoryEnumeration(Enum):
    """
    [a simplified and specialised view of USER PROFILE in TM and NeTEx]
    classification of passengers by age or other factors that may determine the
    fare they will need to pay.
    """

    ADULT = "Adult"
    CHILD = "Child"
    SENIOR = "Senior"
    YOUTH = "Youth"
    DISABLED = "Disabled"
    DOG = "Dog"
    BICYCLE = "Bicycle"
    MOTORCYCLE = "Motorcycle"
    CAR = "Car"
    TRUCK = "Truck"
    GROUP = "Group"
