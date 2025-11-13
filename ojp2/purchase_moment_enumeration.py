from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PurchaseMomentEnumeration(Enum):
    """
    Allowed values for Purchase Moment.

    :cvar ON_RESERVATION: Purchase must be made on reservation in
        advance of travel.
    :cvar IN_ADVANCE: Purchase can be made in advance of travel.
    :cvar IN_ADVANCE_ONLY: Purchase can only be made in advance of
        travel (e.g., for season ticket or advance ticket).
    :cvar BEFORE_BOARDING: Purchase can be made before boarding
        transport vehicle.
    :cvar BEFORE_BOARDING_ONLY: Purchase must be made before boarding
        transport vehicle.
    :cvar ON_BOARDING: Purchase can be made when boarding the transport
        vehicle.
    :cvar ON_BOARDING_ONLY: Purchase can only be made when boarding the
        transport vehicle.
    :cvar AFTER_BOARDING: Purchase can be made after boarding transport
        vehicle.
    :cvar ON_CHECK_IN: Purchase can be made on entering transport
        system.
    :cvar ON_CHECK_OUT: Purchase can be made on leaving transport
        system.
    :cvar SUBSCRIPTION_ONLY: Purchase can only be made on subscription.
    :cvar OTHER: Other moment of Purchase.
    """

    ON_RESERVATION = "onReservation"
    IN_ADVANCE = "inAdvance"
    IN_ADVANCE_ONLY = "inAdvanceOnly"
    BEFORE_BOARDING = "beforeBoarding"
    BEFORE_BOARDING_ONLY = "beforeBoardingOnly"
    ON_BOARDING = "onBoarding"
    ON_BOARDING_ONLY = "onBoardingOnly"
    AFTER_BOARDING = "afterBoarding"
    ON_CHECK_IN = "onCheckIn"
    ON_CHECK_OUT = "onCheckOut"
    SUBSCRIPTION_ONLY = "subscriptionOnly"
    OTHER = "other"
