from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FunicularSubmodesOfTransportEnumeration(Enum):
    """Values for Funicular ModesOfTransport: TPEG pti_table_10.

    :cvar UNKNOWN: Submode of transport is not known to the source
        system.
    :cvar FUNICULAR:
    :cvar STREET_CABLE_CAR: (SIRI 2.1)
    :cvar ALL_FUNICULAR_SERVICES:
    :cvar UNDEFINED_FUNICULAR: Submode of transport is not supported in
        this list.
    :cvar PTI10_0: DEPRECATED since SIRI 2.1
    :cvar PTI10_1: DEPRECATED since SIRI 2.1
    :cvar PTI10_2: DEPRECATED since SIRI 2.1
    :cvar PTI10_255: DEPRECATED since SIRI 2.1
    :cvar LOC14_2: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    FUNICULAR = "funicular"
    STREET_CABLE_CAR = "streetCableCar"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    UNDEFINED_FUNICULAR = "undefinedFunicular"
    PTI10_0 = "pti10_0"
    PTI10_1 = "pti10_1"
    PTI10_2 = "pti10_2"
    PTI10_255 = "pti10_255"
    LOC14_2 = "loc14_2"
