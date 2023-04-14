from dataclasses import dataclass, field
from typing import Optional
from nova.lese_freizeit_beleg_status_request import LeseFreizeitBelegStatusRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeseFreizeitBelegStatus:
    class Meta:
        name = "leseFreizeitBelegStatus"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    lese_freizeit_beleg_status_request: Optional[LeseFreizeitBelegStatusRequest] = field(
        default=None,
        metadata={
            "name": "leseFreizeitBelegStatusRequest",
            "type": "Element",
            "required": True,
        }
    )
