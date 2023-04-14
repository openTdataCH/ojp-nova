from dataclasses import dataclass, field
from typing import List
from nova.leistungs_druck_daten import LeistungsDruckDaten
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BelegResponse(VertriebsResponse):
    """Die Belegantwort ist das Antwortsobjekt des 4.

    Klangs. Sie enthält für jede übermittelte LeistungId ein Objekt
    DruckDaten in dem alle zum Drucken notwendige Druckattribute
    enthalten sind.
    """
    leistungs_druck_daten: List[LeistungsDruckDaten] = field(
        default_factory=list,
        metadata={
            "name": "leistungsDruckDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
