from dataclasses import dataclass, field
from typing import Optional
from nova.freizeit_kombination_angebots_request import FreizeitKombinationAngebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleFreizeitKombiAngebot:
    class Meta:
        name = "erstelleFreizeitKombiAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[FreizeitKombinationAngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )
