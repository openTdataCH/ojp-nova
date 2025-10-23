from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class GueltigkeitsEinschraenkungTyp(Enum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
