from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class ErneuerungsArtGrund(Enum):
    VERTRAG = "VERTRAG"
    U16 = "U16"
    U18 = "U18"
    TEMP_WOHNSITZ = "TEMP_WOHNSITZ"
    ENTFERNTES_AUSLAND = "ENTFERNTES_AUSLAND"
    GESTUETZT = "GESTUETZT"
