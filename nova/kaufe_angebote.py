from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_kauf_request import AngebotsKaufRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufeAngebote:
    """
    Request-Element für den nachgelagerten Verkauf.
    """
    class Meta:
        name = "kaufeAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_kauf_request: Optional[AngebotsKaufRequest] = field(
        default=None,
        metadata={
            "name": "angebotsKaufRequest",
            "type": "Element",
            "required": True,
        }
    )
