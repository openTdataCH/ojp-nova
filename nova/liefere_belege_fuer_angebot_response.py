from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_beleg_response import AngebotsBelegResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LiefereBelegeFuerAngebotResponse:
    """
    Response-Element für die Beleganfrage auf Basis einer AngebotsId.
    """
    class Meta:
        name = "liefereBelegeFuerAngebotResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_beleg_response: Optional[AngebotsBelegResponse] = field(
        default=None,
        metadata={
            "name": "angebotsBelegResponse",
            "type": "Element",
            "required": True,
        }
    )
