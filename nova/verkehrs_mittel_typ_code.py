from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class VerkehrsMittelTypCode(Enum):
    """Mittels VerkehrsMittelTypCode ist ein VerkehrsMittel eindeutig zu
    identifizieren.

    Diese Klasse ist für Anfragen zu referenzieren. BAHN; BUS; SCHIFF
    """
    BAHN = "BAHN"
    SCHIFF = "SCHIFF"
    BUS = "BUS"
