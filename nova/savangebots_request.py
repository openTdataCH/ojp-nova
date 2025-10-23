from dataclasses import dataclass
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class SavangebotsRequest(VertriebsRequest):
    """Die Klasse SAVAngebotsanfrage ist die abstrakte Basisklasse für alle
    Erneuerungs- und Erstattungs-Angebotsanfragen.

    Sie enthält die leistungsID oder die leistungsReferenz einer bereits
    verkauften und zu erstattenden oder zu erneuernden Leistung. Die
    SAVAngebotsanfrage ihrerseits ist eine Subklasse einer
    Vertriebsanfrage.
    """
    class Meta:
        name = "SAVAngebotsRequest"
