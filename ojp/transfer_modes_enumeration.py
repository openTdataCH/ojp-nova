from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TransferModesEnumeration(Enum):
    """
    MODEs dedicated to peform TRANSFERs.
    """
    WALK = "walk"
    PARK_AND_RIDE = "parkAndRide"
    BIKE_AND_RIDE = "bikeAndRide"
    CAR_HIRE = "carHire"
    BIKE_HIRE = "bikeHire"
    PROTECTED_CONNECTION = "protectedConnection"
    GUARANTEED_CONNECTION = "guaranteedConnection"
    REMAIN_IN_VEHICLE = "remainInVehicle"
    CHANGE_WITHIN_VEHICLE = "changeWithinVehicle"
    CHECK_IN = "checkIn"
    CHECK_OUT = "checkOut"
