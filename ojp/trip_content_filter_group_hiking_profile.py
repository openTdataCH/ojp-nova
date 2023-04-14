from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TripContentFilterGroupHikingProfile(Enum):
    """
    :cvar EASY: Regular hiking/walking in valleys and plains and easy
        mountain trails e.g. yellow hiking signs in Switzerland or blue
        in Germany.
    :cvar MEDIUM: Medium difficulty mountain trails. E.g. white-red-
        white hiking signs in Switzerland or red in Germany.
    :cvar DIFFICULT: Difficult mountain trails. E.g. white-blue-white
        hiking signs in Switzerland or black in Germany.
    """
    EASY = "easy"
    MEDIUM = "medium"
    DIFFICULT = "difficult"
