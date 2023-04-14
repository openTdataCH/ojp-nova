from dataclasses import dataclass, field
from typing import Optional
from nova.stornierungs_response import StornierungsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StorniereLeistungResponse:
    class Meta:
        name = "storniereLeistungResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    stornierungs_response: Optional[StornierungsResponse] = field(
        default=None,
        metadata={
            "name": "stornierungsResponse",
            "type": "Element",
            "required": True,
        }
    )
