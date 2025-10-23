from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class SprachCode(Enum):
    """Die in NOVA unterstützten ISO Sprachcodes gemäss ISO 639-1 (Nur
    Kleinbuchstaben erlaubt).

    Aktuell sind das: de, fr, it, en.
    """
    DE = "de"
    EN = "en"
    FR = "fr"
    IT = "it"
