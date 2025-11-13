from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class OjpgenericProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in case of generic problems with the
    request.

    :cvar OJPGENERIC_REQUESTNOTSUPPORTED: The server does not support
        the specific request (e.g.: MultiPointTripRequest).
    :cvar OJPGENERIC_FEATURENOTSUPPORTED: The server does not support
        the requested feature (e.g.: parameter NotVia in TripRequest).
    :cvar OJPGENERIC_LANGUAGENOTSUPPORTED: For the display of texts
        within the result, the server (at least in the context of this
        request) does not support the requested language.
    :cvar OJPGENERIC_EXCEPTIONFROMREQUESTEDLANGUAGE: When displaying
        texts within the result, the server does not support the
        requested language for all occurring text elements.
    :cvar OJPGENERIC_DATAFRAMEREFNOTAVAILABLE: The server cannot provide
        the requested data frame (data version).
    :cvar OJPGENERIC_SYSTEMID_NOT_FOUND: The server was not able to work
        with the SystemID that was provided.
    :cvar OJPGENERIC_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    OJPGENERIC_REQUESTNOTSUPPORTED = "OJPGENERIC_REQUESTNOTSUPPORTED"
    OJPGENERIC_FEATURENOTSUPPORTED = "OJPGENERIC_FEATURENOTSUPPORTED"
    OJPGENERIC_LANGUAGENOTSUPPORTED = "OJPGENERIC_LANGUAGENOTSUPPORTED"
    OJPGENERIC_EXCEPTIONFROMREQUESTEDLANGUAGE = (
        "OJPGENERIC_EXCEPTIONFROMREQUESTEDLANGUAGE"
    )
    OJPGENERIC_DATAFRAMEREFNOTAVAILABLE = "OJPGENERIC_DATAFRAMEREFNOTAVAILABLE"
    OJPGENERIC_SYSTEMID_NOT_FOUND = "OJPGENERIC_SYSTEMID_NOT_FOUND"
    OJPGENERIC_OTHER = "OJPGENERIC_OTHER"
