from dataclasses import dataclass, field
from typing import List, Optional
from nova.parkplatz import Parkplatz
from nova.strecken_geltungs_bereich import StreckenGeltungsBereich
from nova.weg_angabe import WegAngabe
from nova.zonen_geltungs_bereich import ZonenGeltungsBereich

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GeltungsBereich:
    weg_angabe: List[WegAngabe] = field(
        default_factory=list,
        metadata={
            "name": "wegAngabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    zonen_geltungs_bereich: Optional[ZonenGeltungsBereich] = field(
        default=None,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_geltungs_bereich: Optional[StreckenGeltungsBereich] = field(
        default=None,
        metadata={
            "name": "streckenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    parkplatz: Optional[Parkplatz] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
