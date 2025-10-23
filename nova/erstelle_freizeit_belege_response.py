from dataclasses import dataclass, field
from typing import Optional
from nova.freizeit_beleg_response import FreizeitBelegResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleFreizeitBelegeResponse:
    class Meta:
        name = "erstelleFreizeitBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    freizeit_beleg_response: Optional[FreizeitBelegResponse] = field(
        default=None,
        metadata={
            "name": "freizeitBelegResponse",
            "type": "Element",
            "required": True,
        }
    )
