from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class Operator(Enum):
    """@Deprecated Will be removed in NOVA 15. Definiert, wie im Feld nach dem Suchbegriff gesucht wird (z.B. gleich, grösser oder gleich, kleiner oder gleich)."""
    GLEICH = "GLEICH"
    GROESSER_GLEICH = "GROESSER_GLEICH"
    KLEINER_GLEICH = "KLEINER_GLEICH"
