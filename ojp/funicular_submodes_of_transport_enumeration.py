from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FunicularSubmodesOfTransportEnumeration(Enum):
    """
    Values for Funicular ModesOfTransport: TPEG pti_table_10.
    """
    PTI10_0 = "pti10_0"
    UNKNOWN = "unknown"
    PTI10_1 = "pti10_1"
    LOC14_2 = "loc14_2"
    FUNICULAR = "funicular"
    PTI10_2 = "pti10_2"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    PTI10_255 = "pti10_255"
    UNDEFINED_FUNICULAR = "undefinedFunicular"
