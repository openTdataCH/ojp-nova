from dataclasses import dataclass, field
from typing import List, Optional
from nova.teil_strecke import TeilStrecke
from nova.verkehrs_kanten_sequenz import VerkehrsKantenSequenz

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerkehrsStrecke:
    """
    :ivar tarifierte_strecke:
    :ivar nicht_tarifierte_teil_strecke: Am Weganfang oder Wegende
        entfernte Teilstrecken, die nicht tarifiert wurden.
    :ivar id:
    :ivar externe_verbindungs_referenz_id: externeVerbindungsReferenzId
        werden nur für Angebote geliefert.
    """
    tarifierte_strecke: Optional[VerkehrsKantenSequenz] = field(
        default=None,
        metadata={
            "name": "tarifierteStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    nicht_tarifierte_teil_strecke: List[TeilStrecke] = field(
        default_factory=list,
        metadata={
            "name": "nichtTarifierteTeilStrecke",
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
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
