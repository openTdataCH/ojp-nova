from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class WerbungBestaetigung(Enum):
    WERBUNG = "WERBUNG"
    KEINE_WERBUNG = "KEINE_WERBUNG"
    ROBINSON_LISTE = "ROBINSON_LISTE"
    ZU_BESTAETIGEN = "ZU_BESTAETIGEN"
