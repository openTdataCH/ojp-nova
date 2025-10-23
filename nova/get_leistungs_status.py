from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_status_request import LeistungsStatusRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GetLeistungsStatus:
    class Meta:
        name = "getLeistungsStatus"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_status_request: Optional[LeistungsStatusRequest] = field(
        default=None,
        metadata={
            "name": "leistungsStatusRequest",
            "type": "Element",
            "required": True,
        }
    )
