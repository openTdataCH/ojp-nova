from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class LocationProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to LOCATION requests.

    :cvar LOCATION_NORESULTS: No location objects could be found that
        match the input data.
    :cvar LOCATION_UNSUPPORTEDTYPE: The requested location types are not
        supported by the service.
    :cvar LOCATION_UNSUPPORTEDCOMBINATION: The combination of input data
        (text string, coordinates, geographical restrictions) cannot be
        processed by the service.
    :cvar LOCATION_NOREFINEMENT: The given location object could not be
        refined.
    :cvar LOCATION_USAGEIGNORED: The usage type has been ignored.
    :cvar LOCATION_UNSUPPORTEDPTMODES: The service does not support any
        restrictions by transport modes.
    :cvar LOCATION_UNSUPPORTEDLOCALITY: The service does not support any
        restrictions by localities.
    :cvar LOCATION_UNSUPPORTEDSORTINGMETHOD: The service does not
        support the sorting method. The details should provide a list of
        the allowed methods the service supports.
    :cvar LOCATION_OTHER: A problem has occurred that does not have a
        specific problem type.
    """
    LOCATION_NORESULTS = "LOCATION_NORESULTS"
    LOCATION_UNSUPPORTEDTYPE = "LOCATION_UNSUPPORTEDTYPE"
    LOCATION_UNSUPPORTEDCOMBINATION = "LOCATION_UNSUPPORTEDCOMBINATION"
    LOCATION_NOREFINEMENT = "LOCATION_NOREFINEMENT"
    LOCATION_USAGEIGNORED = "LOCATION_USAGEIGNORED"
    LOCATION_UNSUPPORTEDPTMODES = "LOCATION_UNSUPPORTEDPTMODES"
    LOCATION_UNSUPPORTEDLOCALITY = "LOCATION_UNSUPPORTEDLOCALITY"
    LOCATION_UNSUPPORTEDSORTINGMETHOD = "LOCATION_UNSUPPORTEDSORTINGMETHOD"
    LOCATION_OTHER = "LOCATION_OTHER"
