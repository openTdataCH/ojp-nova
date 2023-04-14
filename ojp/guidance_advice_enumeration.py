from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class GuidanceAdviceEnumeration(Enum):
    """
    various types of guidance advice given to travelle.
    """
    ORIGIN = "origin"
    DESTINATION = "destination"
    CONTINUE = "continue"
    KEEP = "keep"
    TURN = "turn"
    LEAVE = "leave"
    ENTER = "enter"
