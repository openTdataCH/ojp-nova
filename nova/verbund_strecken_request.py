from dataclasses import dataclass, field
from typing import Optional
from nova.verbund_strecken_typ import VerbundStreckenTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbundStreckenRequest:
    """
    :ivar tarif_owner:
    :ivar strecken_typ: KURZSTRECKE; LANGSTRECKE
    :ivar abgangs_haltestelle:
    """
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    strecken_typ: Optional[VerbundStreckenTyp] = field(
        default=None,
        metadata={
            "name": "streckenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgangs_haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "abgangsHaltestelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
