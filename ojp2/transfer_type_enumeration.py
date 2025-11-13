from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TransferTypeEnumeration(Enum):
    """TYPE OF TRANSFER.

    It is a mix between MODE information, MODE OF OPERATION information
    and a more stringent TYPE OF TRANSFER.

    :cvar WALK: The "normal" TransferType. Indicates that the traveler
        walks to the next LEG.
    :cvar SHUTTLE: Indicates that a shuttle service is used for the
        TRANSFER LEG. E.g. between gates in an airport.
    :cvar TAXI: Indicates that the transfer is done by taxi. This type
        should be avoided and the taxi leg should be modelled as a
        ContinuousLeg.
    :cvar PROTECTED_CONNECTION: Indicates that the connection to the
        next leg is specially monitored and usually kept (depending on
        agreements between the operators). Usually, it is used in
        combination with walk.
    :cvar GUARANTEED_CONNECTION: The connection is guaranteed. This
        doesn't apply very often, but e.g., a bus has to bring  people
        from the last train to a different destination. Then it will not
        depart before the train has arrived and the passengers have
        changed. In some cases, guaranteedConnection might be used with
        less strictness.
    :cvar REMAIN_IN_VEHICLE: The next leg is in the same VEHICLE and
        there is no need to change it.
    :cvar CHANGE_WITHIN_VEHICLE: If namely trains are split, it might be
        necessary to be in the right part. This is indicated with this
        value.
    :cvar CHECK_IN: Means that a checkin operation is necessary. This
        usually results in a longer time that can't be justified by the
        length of the transfer leg.
    :cvar CHECK_OUT: Means that a checkout operation is necessary. This
        usually results in a longer time that can't be justified by the
        length of the transfer leg
    :cvar PARK_AND_RIDE: This does not model the car ride. But parking
        the car and getting to the stop may take way longer e.g., in a
        big parking garage. This is a special type of checkIn or
        checkOut.
    :cvar BIKE_AND_RIDE: In the transfer leg additional time may be
        needed to get or stow a bike (e.g., because the BIKE PARKING is
        at a special place). this can be seen as a special type of
        checkIn or checkOut.
    :cvar CAR_HIRE: Time for a car hire is needed. This will make the
        transfer leg to take longer than expected. Can be seen as a
        special case of checkIn.
    :cvar BIKE_HIRE: Time for a bike hire is needed. This will make the
        transfer leg to take longer than expected. Can be seen as a
        special case of checkIn.
    :cvar OTHER: Only to be used when no other type applies.
    """

    WALK = "walk"
    SHUTTLE = "shuttle"
    TAXI = "taxi"
    PROTECTED_CONNECTION = "protectedConnection"
    GUARANTEED_CONNECTION = "guaranteedConnection"
    REMAIN_IN_VEHICLE = "remainInVehicle"
    CHANGE_WITHIN_VEHICLE = "changeWithinVehicle"
    CHECK_IN = "checkIn"
    CHECK_OUT = "checkOut"
    PARK_AND_RIDE = "parkAndRide"
    BIKE_AND_RIDE = "bikeAndRide"
    CAR_HIRE = "carHire"
    BIKE_HIRE = "bikeHire"
    OTHER = "other"
