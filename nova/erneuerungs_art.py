from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class ErneuerungsArt(Enum):
    GESTUETZT = "GESTUETZT"
    AUTOMATISCH = "AUTOMATISCH"
    NICHT_ERNEUERBAR = "NICHT_ERNEUERBAR"
