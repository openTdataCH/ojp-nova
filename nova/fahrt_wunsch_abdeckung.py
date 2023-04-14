from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class FahrtWunschAbdeckung(Enum):
    HINFAHRT = "HINFAHRT"
    RUECKFAHRT = "RUECKFAHRT"
    RETOUR = "RETOUR"
