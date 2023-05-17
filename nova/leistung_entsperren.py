from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_entsperren_request import LeistungEntsperrenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungEntsperren:
    class Meta:
        name = "leistungEntsperren"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_entsperren_request: Optional[LeistungEntsperrenRequest] = field(
        default=None,
        metadata={
            "name": "leistungEntsperrenRequest",
            "type": "Element",
            "required": True,
        }
    )
