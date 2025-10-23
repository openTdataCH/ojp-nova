from dataclasses import dataclass, field
from typing import Optional
from nova.verbindung_tarifierbarkeits_request import VerbindungTarifierbarkeitsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class PruefenVerbindungTarifierbarkeits:
    class Meta:
        name = "pruefenVerbindungTarifierbarkeits"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    verbindung_tarifierbarkeits_request: Optional[VerbindungTarifierbarkeitsRequest] = field(
        default=None,
        metadata={
            "name": "verbindungTarifierbarkeitsRequest",
            "type": "Element",
            "required": True,
        }
    )
