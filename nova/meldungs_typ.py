from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class MeldungsTyp(Enum):
    TECHNISCHER_FEHLER = "TECHNISCHER_FEHLER"
    FEHLER = "FEHLER"
    WARNUNG = "WARNUNG"
    INFORMATION = "INFORMATION"
