from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class UhrzeitEinschraenkungenTyp(Enum):
    MIT_UHRZEITEINSCHRAENKUNGEN = "MIT_UHRZEITEINSCHRAENKUNGEN"
    OHNE_UHRZEITEINSCHRAENKUNGEN = "OHNE_UHRZEITEINSCHRAENKUNGEN"
