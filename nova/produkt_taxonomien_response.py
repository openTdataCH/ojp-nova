from dataclasses import dataclass, field
from typing import List
from nova.produkt_taxonomie import ProduktTaxonomie
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ProduktTaxonomienResponse(VertriebsStammdatenResponse):
    produkt_taxonomie: List[ProduktTaxonomie] = field(
        default_factory=list,
        metadata={
            "name": "produktTaxonomie",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
