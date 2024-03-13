from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class Forciert(Enum):
    FORCIERE_NICHTS = "FORCIERE_NICHTS"
    FORCIERE_ALLES = "FORCIERE_ALLES"
    FORCIERE_NUR_ADRESSE = "FORCIERE_NUR_ADRESSE"
    FORCIERE_NUR_NAME = "FORCIERE_NUR_NAME"
