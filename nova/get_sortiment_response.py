from dataclasses import dataclass, field
from typing import Optional
from nova.sortiment_response import SortimentResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetSortimentResponse:
    class Meta:
        name = "getSortimentResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    sortiment_response: Optional[SortimentResponse] = field(
        default=None,
        metadata={
            "name": "sortimentResponse",
            "type": "Element",
            "required": True,
        }
    )
