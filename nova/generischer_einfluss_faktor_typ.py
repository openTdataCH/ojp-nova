from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class GenerischerEinflussFaktorTyp(Enum):
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    TEXT = "TEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    BOOLEAN = "BOOLEAN"
    LAND = "LAND"
    GELDBETRAG = "GELDBETRAG"
