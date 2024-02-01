from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class KorrespondenzSprachCode(Enum):
    """@Deprecated will be removed in NOVA 15, please use "sprache" instead. Als Korrespondenzsprache sind momentan nur Deutsch, Französisch und Italienisch erlaubt."""
    DE = "de"
    FR = "fr"
    IT = "it"
