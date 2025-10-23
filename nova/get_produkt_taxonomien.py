from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_request import VertriebsStammdatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetProduktTaxonomien:
    class Meta:
        name = "getProduktTaxonomien"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    produkt_taxonomien_request: Optional[VertriebsStammdatenRequest] = field(
        default=None,
        metadata={
            "name": "produktTaxonomienRequest",
            "type": "Element",
            "required": True,
        }
    )
