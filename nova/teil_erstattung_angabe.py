from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class TeilErstattungAngabe(Enum):
    ERSTATTUNGSDATUM = "ERSTATTUNGSDATUM"
    ANZAHL_BENUTZTE_EINHEITEN = "ANZAHL_BENUTZTE_EINHEITEN"
    ANGEBOTSID_BENUTZTER_TEIL = "ANGEBOTSID_BENUTZTER_TEIL"
