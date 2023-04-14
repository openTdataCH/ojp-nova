from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_beleg_request import AngebotsBelegRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LiefereBelegeFuerAngebot:
    """
    Request-Element für die Beleganfrage auf Basis einer AngebotsId.
    """
    class Meta:
        name = "liefereBelegeFuerAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_beleg_request: Optional[AngebotsBelegRequest] = field(
        default=None,
        metadata={
            "name": "angebotsBelegRequest",
            "type": "Element",
            "required": True,
        }
    )
