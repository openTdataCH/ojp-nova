from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_entsperren_vertriebs_response import LeistungEntsperrenVertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungEntsperrenResponse:
    class Meta:
        name = "leistungEntsperrenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_entsperren_response: Optional[LeistungEntsperrenVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leistungEntsperrenResponse",
            "type": "Element",
            "required": True,
        }
    )
