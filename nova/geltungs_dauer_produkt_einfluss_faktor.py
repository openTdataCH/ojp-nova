from dataclasses import dataclass, field
from typing import Optional
from nova.dauer import Dauer

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GeltungsDauerProduktEinflussFaktor:
    entwertungs_zeitraum: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "entwertungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    nutzungs_geltungs_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "nutzungsGeltungsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
