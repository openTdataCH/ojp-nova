from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class WochenTag(Enum):
    MONTAG = "MONTAG"
    DIENSTAG = "DIENSTAG"
    MITTWOCH = "MITTWOCH"
    DONNERSTAG = "DONNERSTAG"
    FREITAG = "FREITAG"
    SAMSTAG = "SAMSTAG"
    SONNTAG = "SONNTAG"
