from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class BookableServiceItemTypeEnumeration(Enum):
    """
    Types of bookable service items.

    :cvar WHEELCHAIR: Space for a wheelchair.
    :cvar MOTORISED_WHEELCHAIR: Space for a motorised wheelchair.
    :cvar FOLDABLE_WHEELCHAIR: Space for storing a foldable wheelchair.
    :cvar WALKING_FRAME: Place suitable for a person with a walking
        frame.
    :cvar PRAM: Space for a pram or pushchair.
    :cvar HEAVY_LUGGAGE: Space for storing heavy luggage.
    :cvar CHILD_SEAT_TAKEN_ALONG: Seat suitable for attaching a child
        seat taken along by the passengers.
    :cvar CHILD_SEAT_SUPPLIED: Child seat provided in the vehicle.
    :cvar BABY_CARRIER_TAKEN_ALONG: Seat suitable for attaching a baby
        carrier taken along by the passengers.
    :cvar BABY_CARRIER_SUPPLIED: Baby carrier provided in the vehicle.
    :cvar SEAT_BOOSTER_SUPPLIED: Seat booster provided in the vehicle.
    :cvar BICYCLE: Space for a bicycle.
    :cvar GUIDE_DOG: Place suitable when accompanied by a guide dog.
    :cvar DOG: Place suitable when accompanied by a dog.
    :cvar BOARDING_ASSISTANCE: Assistance for boarding.
    :cvar ALIGHTING_ASSISTANCE: Assistance for alighting.
    :cvar ONBOARD_ASSISTANCE: Assistance available on board, during the
        journey.
    :cvar UNASSISTED_MINOR_ASSISTANCE: Assistance for a minor travelling
        alone.
    """

    WHEELCHAIR = "wheelchair"
    MOTORISED_WHEELCHAIR = "motorisedWheelchair"
    FOLDABLE_WHEELCHAIR = "foldableWheelchair"
    WALKING_FRAME = "walkingFrame"
    PRAM = "pram"
    HEAVY_LUGGAGE = "heavyLuggage"
    CHILD_SEAT_TAKEN_ALONG = "childSeatTakenAlong"
    CHILD_SEAT_SUPPLIED = "childSeatSupplied"
    BABY_CARRIER_TAKEN_ALONG = "babyCarrierTakenAlong"
    BABY_CARRIER_SUPPLIED = "babyCarrierSupplied"
    SEAT_BOOSTER_SUPPLIED = "seatBoosterSupplied"
    BICYCLE = "bicycle"
    GUIDE_DOG = "guideDog"
    DOG = "dog"
    BOARDING_ASSISTANCE = "boardingAssistance"
    ALIGHTING_ASSISTANCE = "alightingAssistance"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNASSISTED_MINOR_ASSISTANCE = "unassistedMinorAssistance"
