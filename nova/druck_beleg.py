from dataclasses import dataclass, field
from typing import List, Optional
from nova.druck_attribut import DruckAttribut
from nova.traeger_medium_typ import TraegerMediumTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class DruckBeleg:
    traeger_medium_typ: Optional[TraegerMediumTyp] = field(
        default=None,
        metadata={
            "name": "traegerMediumTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    druck_attribut: List[DruckAttribut] = field(
        default_factory=list,
        metadata={
            "name": "druckAttribut",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    beleg_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "belegId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )
    beleg_typ: Optional[str] = field(
        default=None,
        metadata={
            "name": "belegTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_inclusive": 0,
        }
    )
