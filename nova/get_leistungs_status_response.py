from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_status_response import LeistungsStatusResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GetLeistungsStatusResponse:
    class Meta:
        name = "getLeistungsStatusResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_status_response: Optional[LeistungsStatusResponse] = field(
        default=None,
        metadata={
            "name": "leistungsStatusResponse",
            "type": "Element",
            "required": True,
        }
    )
