from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class ReisendenTypCode(Enum):
    """
    PERSON; HUND; VELO.
    """
    PERSON = "PERSON"
    HUND = "HUND"
    VELO = "VELO"
