from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_request import AngebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleAngebote:
    """Request-Element für den 1.

    Klang
    """
    class Meta:
        name = "erstelleAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[AngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )
