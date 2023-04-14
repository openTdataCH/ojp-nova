from dataclasses import dataclass, field
from typing import Optional
from nova.bestaetige_produktion_vertriebs_response import BestaetigeProduktionVertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BestaetigeProduktionResponse:
    """
    Response-Element für die abschliessende Bestätigung der Produktion.
    """
    class Meta:
        name = "bestaetigeProduktionResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    bestaetige_produktion_response: Optional[BestaetigeProduktionVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "bestaetigeProduktionResponse",
            "type": "Element",
            "required": True,
        }
    )
