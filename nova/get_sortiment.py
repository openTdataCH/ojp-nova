from dataclasses import dataclass, field
from typing import Optional
from nova.sortiment_request import SortimentRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetSortiment:
    class Meta:
        name = "getSortiment"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    sortiment_request: Optional[SortimentRequest] = field(
        default=None,
        metadata={
            "name": "sortimentRequest",
            "type": "Element",
            "required": True,
        }
    )
