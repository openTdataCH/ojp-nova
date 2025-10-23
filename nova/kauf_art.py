from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class KaufArt(Enum):
    ERSTKAUF = "ERSTKAUF"
    FOLGEKAUF = "FOLGEKAUF"
