from dataclasses import dataclass, field
from typing import Optional
from nova.beleg_response import BelegResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleBelegeResponse:
    """Response-Element für den 4.

    Klang
    """
    class Meta:
        name = "erstelleBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    beleg_response: Optional[BelegResponse] = field(
        default=None,
        metadata={
            "name": "belegResponse",
            "type": "Element",
            "required": True,
        }
    )
