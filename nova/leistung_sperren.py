from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_sperren_request import LeistungSperrenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungSperren:
    class Meta:
        name = "leistungSperren"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_sperren_request: Optional[LeistungSperrenRequest] = field(
        default=None,
        metadata={
            "name": "leistungSperrenRequest",
            "type": "Element",
            "required": True,
        }
    )
