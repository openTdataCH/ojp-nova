from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_response import AngebotsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleTarifWegKombinationsAngebotResponse:
    class Meta:
        name = "erstelleTarifWegKombinationsAngebotResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_response: Optional[AngebotsResponse] = field(
        default=None,
        metadata={
            "name": "angebotsResponse",
            "type": "Element",
            "required": True,
        }
    )
