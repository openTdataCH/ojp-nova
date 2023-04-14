from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_sperren_vertriebs_response import LeistungSperrenVertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungSperrenResponse:
    class Meta:
        name = "leistungSperrenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_sperren_response: Optional[LeistungSperrenVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leistungSperrenResponse",
            "type": "Element",
            "required": True,
        }
    )
