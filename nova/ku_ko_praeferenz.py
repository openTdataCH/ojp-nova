from dataclasses import dataclass, field
from typing import Optional
from nova.ku_ko_massnahme import KuKoMassnahme
from nova.ku_ko_medium import KuKoMedium

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class KuKoPraeferenz:
    ku_ko_massnahme: Optional[KuKoMassnahme] = field(
        default=None,
        metadata={
            "name": "kuKoMassnahme",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    ku_ko_medium: Optional[KuKoMedium] = field(
        default=None,
        metadata={
            "name": "kuKoMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
