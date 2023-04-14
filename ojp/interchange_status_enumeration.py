from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class InterchangeStatusEnumeration(Enum):
    """
    Values for Interchange Status TPEG cross reference pti_table 31.
    """
    PTI31_0 = "pti31_0"
    UNKNOWN = "unknown"
    PTI31_1 = "pti31_1"
    CONNECTION = "connection"
    PTI31_2 = "pti31_2"
    REPLACEMENT = "replacement"
    PTI31_3 = "pti31_3"
    ALTERNATIVE = "alternative"
    PTI31_4 = "pti31_4"
    CONNECTION_NOT_HELD = "connectionNotHeld"
    PTI31_5 = "pti31_5"
    CONNECTION_HELD = "connectionHeld"
    PTI31_6 = "pti31_6"
    STATUS_OF_CONENCTION_UNDECIDED = "statusOfConenctionUndecided"
    PTI31_255 = "pti31_255"
    UNDEFINED_CROSS_REFERENCE_INFORMATION = "undefinedCrossReferenceInformation"
