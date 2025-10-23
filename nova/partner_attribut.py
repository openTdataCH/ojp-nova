from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class PartnerAttribut(Enum):
    ADRESSE = "ADRESSE"
    EMAIL = "EMAIL"
    FESTNETZ = "FESTNETZ"
    GEBURTSDATUM = "GEBURTSDATUM"
    GESCHLECHT = "GESCHLECHT"
    MOBILE = "MOBILE"
    NAME = "NAME"
    WERBUNG = "WERBUNG"
    SPRACHE = "SPRACHE"
