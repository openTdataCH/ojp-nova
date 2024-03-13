from dataclasses import dataclass, field
from typing import List, Optional
from nova.verbindungs_abschnitt import VerbindungsAbschnitt

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbindungsInfo:
    verbindungs_abschnitt: List[VerbindungsAbschnitt] = field(
        default_factory=list,
        metadata={
            "name": "verbindungsAbschnitt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
