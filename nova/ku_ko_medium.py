from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


class KuKoMedium(Enum):
    """@Deprecated will be removed in NOVA 15."""
    BRIEF = "BRIEF"
    EMAIL = "EMAIL"
    SMS = "SMS"
    INAKTIV = "INAKTIV"
