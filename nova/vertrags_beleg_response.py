from dataclasses import dataclass, field
from typing import List
from nova.vertrags_daten import VertragsDaten
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertragsBelegResponse(VertriebsResponse):
    vertrags_daten: List[VertragsDaten] = field(
        default_factory=list,
        metadata={
            "name": "vertragsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
