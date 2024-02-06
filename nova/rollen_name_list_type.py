from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class RollenNameListType:
    """
    Type defines a not empty list of role names.
    """
    rolle: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_occurs": 1,
            "min_length": 0,
            "max_length": 64,
        }
    )
