from dataclasses import dataclass, field
from typing import Optional
from nova.platz import Platz
from nova.reservierter_verbindungs_abschnitt import ReservierterVerbindungsAbschnitt

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ReservationsInfo:
    platz: Optional[Platz] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reservierter_verbindungs_abschnitt: Optional[ReservierterVerbindungsAbschnitt] = field(
        default=None,
        metadata={
            "name": "reservierterVerbindungsAbschnitt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
