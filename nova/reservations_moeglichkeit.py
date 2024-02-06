from dataclasses import dataclass, field
from typing import List, Optional
from nova.platz_verfuegbarkeit import PlatzVerfuegbarkeit

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ReservationsMoeglichkeit:
    platz_verfuegbarkeit: List[PlatzVerfuegbarkeit] = field(
        default_factory=list,
        metadata={
            "name": "platzVerfuegbarkeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    verbindungs_abschnitt_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "verbindungsAbschnittIdRef",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
