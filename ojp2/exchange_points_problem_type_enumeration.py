from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class ExchangePointsProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to EXCHANGE POINTS
    requests.

    :cvar EXCHANGEPOINTS_NORESULTS: No exchange points could be found
        that match the query criteria.
    :cvar EXCHANGEPOINTS_UNKNOWNDESTINATIONSYSTEM: The destination
        system given in the request parameters is unknown.
    :cvar EXCHANGEPOINTS_UNKNOWNADJACENTSYSTEM: One or more of the
        adjacent systems given in the request parameters are unknown.
    :cvar EXCHANGEPOINTS_OTHER: A problem has occurred that does not
        have a specific problem type.
    """

    EXCHANGEPOINTS_NORESULTS = "EXCHANGEPOINTS_NORESULTS"
    EXCHANGEPOINTS_UNKNOWNDESTINATIONSYSTEM = (
        "EXCHANGEPOINTS_UNKNOWNDESTINATIONSYSTEM"
    )
    EXCHANGEPOINTS_UNKNOWNADJACENTSYSTEM = (
        "EXCHANGEPOINTS_UNKNOWNADJACENTSYSTEM"
    )
    EXCHANGEPOINTS_OTHER = "EXCHANGEPOINTS_OTHER"
