from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class PagingParameter:
    """
    Trefferanzahl und -offset für die Suche.
    """
    max_treffer: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxTreffer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_inclusive": 0,
        }
    )
    treffer_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "trefferOffset",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_inclusive": 0,
        }
    )
