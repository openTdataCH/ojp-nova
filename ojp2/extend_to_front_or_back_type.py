from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class ExtendToFrontOrBackType(Enum):
    """
    Prefer earlier or later times.
    """

    EXTEND_TO_FRONT = "extendToFront"
    EXTEND_TO_BACK = "extendToBack"
