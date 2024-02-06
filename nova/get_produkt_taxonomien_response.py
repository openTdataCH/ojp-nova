from dataclasses import dataclass, field
from typing import Optional
from nova.produkt_taxonomien_response import ProduktTaxonomienResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetProduktTaxonomienResponse:
    class Meta:
        name = "getProduktTaxonomienResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    produkt_taxonomien_response: Optional[ProduktTaxonomienResponse] = field(
        default=None,
        metadata={
            "name": "produktTaxonomienResponse",
            "type": "Element",
            "required": True,
        }
    )
