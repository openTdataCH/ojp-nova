from dataclasses import dataclass, field
from typing import Optional
from nova.offerten_response import OffertenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class OfferiereLeistungenResponse:
    """Response-Element für den 2.

    Klang
    """
    class Meta:
        name = "offeriereLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    offerten_response: Optional[OffertenResponse] = field(
        default=None,
        metadata={
            "name": "offertenResponse",
            "type": "Element",
            "required": True,
        }
    )
