from dataclasses import dataclass, field
from typing import List, Optional
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeseFreizeitBelegStatusRequest(VertriebsRequest):
    leistung: List["LeseFreizeitBelegStatusRequest.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        traeger_medium_code: List[str] = field(
            default_factory=list,
            metadata={
                "name": "traegerMediumCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
