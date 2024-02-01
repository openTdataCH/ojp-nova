from dataclasses import dataclass, field
from typing import List
from nova.abstract_einschraenkung import AbstractEinschraenkung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ZonenEinschraenkung(AbstractEinschraenkung):
    zone_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "zoneRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "tokens": True,
        }
    )
