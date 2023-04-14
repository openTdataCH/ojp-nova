from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class RaeumlicheFlexibilitaet(Enum):
    VERBINDUNG = "VERBINDUNG"
    STRECKE = "STRECKE"
    ZONEN = "ZONEN"
    STRECKE_UND_ZONEN = "STRECKE_UND_ZONEN"
    VERBUND = "VERBUND"
    NATIONAL = "NATIONAL"
