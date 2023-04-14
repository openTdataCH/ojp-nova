from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class AusgabeStatusTyp(Enum):
    NICHT_GEDRUCKT = "NICHT_GEDRUCKT"
    DRUCK_ERFOLGREICH = "DRUCK_ERFOLGREICH"
    DRUCK_ERFOLGREICH_IMMUTABLE = "DRUCK_ERFOLGREICH_IMMUTABLE"
