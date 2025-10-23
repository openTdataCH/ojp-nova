from dataclasses import dataclass, field
from typing import Optional
from nova.liefere_belege_fuer_angebot import LiefereBelegeFuerAngebot

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        liefere_belege_fuer_angebot: Optional[LiefereBelegeFuerAngebot] = field(
            default=None,
            metadata={
                "name": "liefereBelegeFuerAngebot",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
