from dataclasses import dataclass, field
from typing import List, Optional
from nova.dauer import Dauer
from nova.kante import Kante

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerkehrsKantenSequenz:
    """Die VerkehrskantenSequenz enthält eine Sequenz von Verkehrskanten.

    Die VerkehrskantenSequenz enthält alle Kanten des Wegs, die für das
    Angebot gefundenen wurden und VerkehrsMitteltyp fuer jede Kante.
    """
    kante: List[Kante] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    schnellste_reise_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "schnellsteReiseDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
