from dataclasses import dataclass, field
from typing import List
from nova.zahlungs_attribut_2 import ZahlungsAttribut2

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ZahlungsAttribute:
    zahlungs_attribut: List[ZahlungsAttribut2] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsAttribut",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
