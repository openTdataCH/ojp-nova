from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class ZahlungsIntervall(Enum):
    MONATLICH = "MONATLICH"
    JAEHRLICH = "JAEHRLICH"
