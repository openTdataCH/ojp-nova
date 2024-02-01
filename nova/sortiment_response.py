from dataclasses import dataclass, field
from typing import List
from nova.sortiment import Sortiment
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class SortimentResponse(VertriebsStammdatenResponse):
    sortiment: List[Sortiment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
