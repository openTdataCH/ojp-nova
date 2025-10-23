from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


class KlassenTypCode(Enum):
    """Der KlassenTypCode enthält die Klassenspanne für den anfragenden
    Leistungsvermittler, das heisst die Menge aller wählbaren Klassen.

    KLASSE_1; KLASSE_2; KLASSENWECHSEL Mittels KlassenTypCode ist eine
    Klasse eindeutig zu identifizieren. Diese Klasse ist für Anfragen zu
    referenzieren.
    """
    KLASSE_1 = "KLASSE_1"
    KLASSE_2 = "KLASSE_2"
    KLASSENWECHSEL = "KLASSENWECHSEL"
