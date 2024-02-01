from dataclasses import dataclass, field
from typing import List
from nova.kunden_segment import KundenSegment

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenKundenSegmente:
    kunden_segment: List[KundenSegment] = field(
        default_factory=list,
        metadata={
            "name": "kundenSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
