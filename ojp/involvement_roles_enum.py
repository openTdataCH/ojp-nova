from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class InvolvementRolesEnum(Enum):
    CYCLIST = "cyclist"
    PEDESTRIAN = "pedestrian"
    UNKNOWN = "unknown"
    VEHICLE_DRIVER = "vehicleDriver"
    VEHICLE_OCCUPANT = "vehicleOccupant"
    VEHICLE_PASSENGER = "vehiclePassenger"
    WITNESS = "witness"
