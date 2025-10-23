from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_request import VertriebsStammdatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class SortimentRequest(VertriebsStammdatenRequest):
    vertriebs_punkt: Optional[int] = field(
        default=None,
        metadata={
            "name": "vertriebsPunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 99999,
        }
    )
