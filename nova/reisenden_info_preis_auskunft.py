from dataclasses import dataclass, field
from typing import List, Optional
from nova.reisenden_typ_code import ReisendenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class ReisendenInfoPreisAuskunft:
    ermaessigungs_karte_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ermaessigungsKarteCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_length": 0,
            "max_length": 50,
        }
    )
    alter: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 200,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    reisenden_typ: Optional[ReisendenTypCode] = field(
        default=None,
        metadata={
            "name": "reisendenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
