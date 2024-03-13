from dataclasses import dataclass, field
from typing import List, Optional
from nova.preis import Preis

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstattungsGebuehr:
    zu_erstattende_leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "zuErstattendeLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    gebuehr: Optional[Preis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
