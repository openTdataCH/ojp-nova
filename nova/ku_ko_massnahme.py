from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class KuKoMassnahme(Enum):
    """@Deprecated will be removed in NOVA 15."""
    RECHNUNG = "RECHNUNG"
    ERNEUERUNG_JAHRESABO = "ERNEUERUNG_JAHRESABO"
    ERNEUERUNG_MONATSABO = "ERNEUERUNG_MONATSABO"
    ERINNERUNG_ALLGEMEIN = "ERINNERUNG_ALLGEMEIN"
    ERINNERUNG_LKT = "ERINNERUNG_LKT"
