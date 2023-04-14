from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class TarifKlasse(Enum):
    DV = "DV"
    VERBUND = "VERBUND"
    IP = "IP"
    INTER = "INTER"
    FREIZEIT = "FREIZEIT"
    SERVICE = "SERVICE"
    TU_TARIF = "TU_TARIF"
    VERBUNDERWEITERUNG = "VERBUNDERWEITERUNG"
