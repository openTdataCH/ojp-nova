from dataclasses import dataclass, field
from typing import List, Optional
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StornierungsRequest(VertriebsRequest):
    """
    Diese Klasse dient als Container für die zu stornierende Leistung.
    """
    leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    stornierungs_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "stornierungsGrund",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
