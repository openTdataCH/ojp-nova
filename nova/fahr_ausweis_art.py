from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class FahrAusweisArt(Enum):
    EINZELBILLETT = "EINZELBILLETT"
    MEHRFAHRTENKARTE = "MEHRFAHRTENKARTE"
    ABONNEMENT = "ABONNEMENT"
    GRUPPE = "GRUPPE"
