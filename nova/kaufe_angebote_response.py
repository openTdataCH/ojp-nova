from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_kauf_response import AngebotsKaufResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufeAngeboteResponse:
    """
    Response-Element für den nachgelagerten Verkauf.
    """
    class Meta:
        name = "kaufeAngeboteResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_kauf_response: Optional[AngebotsKaufResponse] = field(
        default=None,
        metadata={
            "name": "angebotsKaufResponse",
            "type": "Element",
            "required": True,
        }
    )
