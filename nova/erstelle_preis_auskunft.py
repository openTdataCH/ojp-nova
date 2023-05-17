from dataclasses import dataclass, field
from typing import Optional
from nova.preis_auskunft_request import PreisAuskunftRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class ErstellePreisAuskunft:
    class Meta:
        name = "erstellePreisAuskunft"
        namespace = "http://nova.voev.ch/services/v14/preisauskunft"

    preis_auskunft_request: Optional[PreisAuskunftRequest] = field(
        default=None,
        metadata={
            "name": "PreisAuskunftRequest",
            "type": "Element",
            "required": True,
        }
    )
