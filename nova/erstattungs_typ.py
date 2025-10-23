from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class ErstattungsTyp(Enum):
    VOLLERSTATTUNG = "VOLLERSTATTUNG"
    TEILERSTATTUNG = "TEILERSTATTUNG"
    ANNULLATION = "ANNULLATION"
    HINTERLEGUNG = "HINTERLEGUNG"
