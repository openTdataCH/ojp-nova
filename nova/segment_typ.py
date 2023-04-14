from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class SegmentTyp(Enum):
    HALTESTELLE = "HALTESTELLE"
    INFO = "INFO"
    VERKEHRSMITTEL_TYP = "VERKEHRSMITTEL_TYP"
    TU = "TU"
    SEPARATOR = "SEPARATOR"
    ZONE = "ZONE"
    FAHRART = "FAHRART"
    VIA = "VIA"
    VERBUND = "VERBUND"
    LOKALNETZ = "LOKALNETZ"
    IP_VIATEXT = "IP_VIATEXT"
