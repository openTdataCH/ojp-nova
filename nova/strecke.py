from dataclasses import dataclass

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Strecke:
    """
    Die Klasse Strecke ist die abstrakte Basisklasse für alle Arten von Strecken
    (Wege oder Fahrplanverbindungen).
    """
