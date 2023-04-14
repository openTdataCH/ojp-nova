from dataclasses import dataclass, field
from typing import Optional
from nova.offerten_request import OffertenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class OfferiereLeistungen:
    """Request-Element für den 2.

    Klang
    """
    class Meta:
        name = "offeriereLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    offerten_request: Optional[OffertenRequest] = field(
        default=None,
        metadata={
            "name": "offertenRequest",
            "type": "Element",
            "required": True,
        }
    )
