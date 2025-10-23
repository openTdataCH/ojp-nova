from dataclasses import dataclass, field
from typing import Optional
from nova.get_aktuellen_daten_release import GetAktuellenDatenRelease

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_aktuellen_daten_release: Optional[GetAktuellenDatenRelease] = field(
            default=None,
            metadata={
                "name": "getAktuellenDatenRelease",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
