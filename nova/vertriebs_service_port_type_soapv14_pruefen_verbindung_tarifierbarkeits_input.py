from dataclasses import dataclass, field
from typing import Optional
from nova.pruefen_verbindung_tarifierbarkeits import PruefenVerbindungTarifierbarkeits

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        pruefen_verbindung_tarifierbarkeits: Optional[PruefenVerbindungTarifierbarkeits] = field(
            default=None,
            metadata={
                "name": "pruefenVerbindungTarifierbarkeits",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
