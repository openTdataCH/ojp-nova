from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class FahrArtTypCode(Enum):
    """Mittels FahrartTypCode ist ein FahrartTyp eindeutig zu identifizieren.

    Diese Klasse ist für Anfragen zu referenzieren. Der Fahrarttyp
    enthält alle wählbaren Fahrarten: EINFACH; RETOUR; RUNDFAHRT
    """
    EINFACH = "EINFACH"
    RETOUR = "RETOUR"
    RUNDFAHRT = "RUNDFAHRT"
