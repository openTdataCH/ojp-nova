from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TripChangeProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to TRIPCHANGE requests.

    :cvar TRIPCHANGE_NOLATERTRIPFOUND: No later option for the requested
        part of the TRIP could be found.
    :cvar TRIPCHANGE_NOEARLIERTRIPFOUND: No earlier option for the
        requested part of the TRIP could be found.
    :cvar TRIPCHANGE_INVALIDLEGREF: Requested leg ref is invalid.
    :cvar TRIPCHANGE_INVALIDOPERATOR: Requested operator is invalid.
    :cvar TRIPCHANGE_NOVEHICLEAVAILABLE: No vehicle is available for the
        requested leg.
    :cvar TRIPCHANGE_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    TRIPCHANGE_NOLATERTRIPFOUND = "TRIPCHANGE_NOLATERTRIPFOUND"
    TRIPCHANGE_NOEARLIERTRIPFOUND = "TRIPCHANGE_NOEARLIERTRIPFOUND"
    TRIPCHANGE_INVALIDLEGREF = "TRIPCHANGE_INVALIDLEGREF"
    TRIPCHANGE_INVALIDOPERATOR = "TRIPCHANGE_INVALIDOPERATOR"
    TRIPCHANGE_NOVEHICLEAVAILABLE = "TRIPCHANGE_NOVEHICLEAVAILABLE"
    TRIPCHANGE_OTHER = "TRIPCHANGE_OTHER"
