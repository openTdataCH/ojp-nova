from dataclasses import dataclass, field
from typing import List
from nova.zahlungs_art import ZahlungsArt

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ZahlungsArten:
    zahlungs_art: List[ZahlungsArt] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsArt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
