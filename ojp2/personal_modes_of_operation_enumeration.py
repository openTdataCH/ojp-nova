from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class PersonalModesOfOperationEnumeration(Enum):
    """
    PERSONAL MODE OF OPERATION.

    :cvar SELF: Without a VEHICLE.
    :cvar OWN: Using an owned VEHICLE.
    :cvar OTHER_OWNED: Using a VEHICLE owned by a different private
        person without a commercial context.
    :cvar PRIVATE_LIFT: Other driver without commercial interest is
        driving. Typical case of being picked up or dropped off at a
        stop e.g., by a friend, relative. If the offer is advertised or
        commercial, then pooling from ALTERNATIVE MODE OF OPERATION
        should be chosen.
    :cvar LEASE: Using a leased VEHICLE.
    """

    SELF = "self"
    OWN = "own"
    OTHER_OWNED = "otherOwned"
    PRIVATE_LIFT = "privateLift"
    LEASE = "lease"
