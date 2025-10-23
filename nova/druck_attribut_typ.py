from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class DruckAttributTyp(Enum):
    TEXT = "TEXT"
    LOCALIZEDTEXT = "LOCALIZEDTEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    BINARY = "BINARY"
    GELDBETRAG = "GELDBETRAG"
    WEGANGABE = "WEGANGABE"
    BOOLEAN = "BOOLEAN"
    REISEWEGINFO = "REISEWEGINFO"
