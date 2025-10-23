from dataclasses import dataclass, field
from typing import Optional
from nova.bestaetige_produktion_request import BestaetigeProduktionRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BestaetigeProduktion:
    """
    Request-Element für die abschliessende Bestätigung der Produktion.
    """
    class Meta:
        name = "bestaetigeProduktion"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    bestaetige_produktion_request: Optional[BestaetigeProduktionRequest] = field(
        default=None,
        metadata={
            "name": "bestaetigeProduktionRequest",
            "type": "Element",
            "required": True,
        }
    )
