from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class VerkaufsParameterWertTyp(Enum):
    """
    Enumeration aller möglichen VerkaufsParameter.
    """
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    TEXT = "TEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    BOOLEAN = "BOOLEAN"
    TKID = "TKID"
    ADRESSE = "ADRESSE"
    NAMEVORNAME = "NAMEVORNAME"
    LAND = "LAND"
