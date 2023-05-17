from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class SperrTyp(Enum):
    """
    Enumeration aller Typen von Sperren.
    """
    NUTZUNG = "NUTZUNG"
    ERSTATTUNG = "ERSTATTUNG"
    HINTERLEGUNG = "HINTERLEGUNG"
