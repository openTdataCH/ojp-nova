from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class VatRateEnumeration(Enum):
    """
    Enumeration of Value Added Tax rates.
    """
    NO = "no"
    FULL = "full"
    HALF = "half"
    MIXED = "mixed"
    UNKNOWN = "unknown"
