from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class ZeitEinheitCode(Enum):
    """Code der eine Zeiteinheit eindeutig identifiziert.

    MINUTEN; STUNDEN; TAGE; WOCHEN; MONATE; JAHRE
    """
    MINUTEN = "MINUTEN"
    STUNDEN = "STUNDEN"
    TAGE = "TAGE"
    WOCHEN = "WOCHEN"
    MONATE = "MONATE"
    JAHRE = "JAHRE"
