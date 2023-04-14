from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TrainElementTypeEnumeration(Enum):
    """Allowed values for TYPE OF TRAIN ELEMENT.

    (since SIRI 2.1)
    """
    BUFFET_CAR = "buffetCar"
    CARRIAGE = "carriage"
    ENGINE = "engine"
    CAR_TRANSPORTER = "carTransporter"
    SLEEPER_CARRIAGE = "sleeperCarriage"
    LUGGAGE_VAN = "luggageVan"
    RESTAURANT_CARRIAGE = "restaurantCarriage"
    OTHER = "other"
