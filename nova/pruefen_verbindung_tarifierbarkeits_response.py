from dataclasses import dataclass, field
from typing import Optional
from nova.verbindung_tarifierbarkeits_response import VerbindungTarifierbarkeitsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class PruefenVerbindungTarifierbarkeitsResponse:
    class Meta:
        name = "pruefenVerbindungTarifierbarkeitsResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    verbindung_tarifierbarkeits_response: Optional[VerbindungTarifierbarkeitsResponse] = field(
        default=None,
        metadata={
            "name": "verbindungTarifierbarkeitsResponse",
            "type": "Element",
            "required": True,
        }
    )
