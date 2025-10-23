from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class LeistungsTypCode(Enum):
    """
    Enum der möglichen Typen von Leistungen.
    """
    VERKAUF = "VERKAUF"
    ERSTATTUNG = "ERSTATTUNG"
    ANNULLATION = "ANNULLATION"
    ANNULLATION_ERSTATTUNG = "ANNULLATION_ERSTATTUNG"
    HINTERLEGUNG = "HINTERLEGUNG"
    AKTIVIERUNG = "AKTIVIERUNG"
