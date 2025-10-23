from dataclasses import dataclass, field
from typing import Optional
from nova.get_produkt_taxonomien_response import GetProduktTaxonomienResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_produkt_taxonomien_response: Optional[GetProduktTaxonomienResponse] = field(
            default=None,
            metadata={
                "name": "getProduktTaxonomienResponse",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        fault: Optional["VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
