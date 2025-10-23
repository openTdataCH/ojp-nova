from dataclasses import dataclass, field
from typing import Optional
from nova.preis_auskunft_response import PreisAuskunftResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class ErstellePreisAuskunftResponse:
    class Meta:
        name = "erstellePreisAuskunftResponse"
        namespace = "http://nova.voev.ch/services/v14/preisauskunft"

    preis_auskunft_response: Optional[PreisAuskunftResponse] = field(
        default=None,
        metadata={
            "name": "preisAuskunftResponse",
            "type": "Element",
            "required": True,
        }
    )
