from dataclasses import dataclass, field
from typing import List, Optional
from nova.angebots_kauf_request_param import AngebotsKaufRequestParam
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsKaufRequest(VertriebsRequest):
    leistungs_request: List[AngebotsKaufRequestParam] = field(
        default_factory=list,
        metadata={
            "name": "leistungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
