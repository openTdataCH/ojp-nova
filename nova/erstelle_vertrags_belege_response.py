from dataclasses import dataclass, field
from typing import Optional
from nova.vertrags_beleg_response import VertragsBelegResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleVertragsBelegeResponse:
    class Meta:
        name = "erstelleVertragsBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    vertrags_beleg_response: Optional[VertragsBelegResponse] = field(
        default=None,
        metadata={
            "name": "vertragsBelegResponse",
            "type": "Element",
            "required": True,
        }
    )
