from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class AltersBereich:
    """
    :ivar min_alter: Inklusive Angabe. minAlter=6 bedeutet "ab 6
        Jahren".
    :ivar max_alter: Exklusive Angabe. maxAlter=16 bedeutet "unter 16
        Jahren" (="bis und mit 15 Jahren").
    """
    min_alter: Optional[int] = field(
        default=None,
        metadata={
            "name": "minAlter",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
            "max_inclusive": 200,
        }
    )
    max_alter: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxAlter",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
            "max_inclusive": 200,
        }
    )
