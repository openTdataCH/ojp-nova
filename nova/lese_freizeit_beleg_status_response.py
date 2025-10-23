from dataclasses import dataclass, field
from typing import Optional
from nova.lese_freizeit_beleg_status_vertriebs_response import LeseFreizeitBelegStatusVertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeseFreizeitBelegStatusResponse:
    class Meta:
        name = "leseFreizeitBelegStatusResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    lese_freizeit_beleg_status_response: Optional[LeseFreizeitBelegStatusVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leseFreizeitBelegStatusResponse",
            "type": "Element",
            "required": True,
        }
    )
