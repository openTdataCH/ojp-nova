from dataclasses import dataclass, field
from typing import List, Optional
from nova.zonen_tarif_stufe import ZonenTarifStufe

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ZonenTarif:
    zonen_plan_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "zonenPlanRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    tarif_stufe: List[ZonenTarifStufe] = field(
        default_factory=list,
        metadata={
            "name": "tarifStufe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    verbund: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    nova_zonen_tarif_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "novaZonenTarifCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 255,
        }
    )
