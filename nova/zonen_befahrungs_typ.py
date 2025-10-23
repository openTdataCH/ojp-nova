from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class ZonenBefahrungsTyp(Enum):
    RAUMZEIT = "RAUMZEIT"
    STRECKEZEIT = "STRECKEZEIT"
