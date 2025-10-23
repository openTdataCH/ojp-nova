from dataclasses import dataclass, field
from typing import List
from nova.erstattungs_bedingung import ErstattungsBedingung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenErstattungsBedingungen:
    erstattungs_bedingung: List[ErstattungsBedingung] = field(
        default_factory=list,
        metadata={
            "name": "erstattungsBedingung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
