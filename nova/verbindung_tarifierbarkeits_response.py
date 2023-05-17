from dataclasses import dataclass, field
from typing import List, Optional
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbindungTarifierbarkeitsResponse(VertriebsResponse):
    ist_tarifierbar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istTarifierbar",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    produkt_nummer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "produktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
