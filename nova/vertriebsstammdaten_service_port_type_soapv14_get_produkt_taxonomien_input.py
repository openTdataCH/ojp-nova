from dataclasses import dataclass, field
from typing import Optional
from nova.get_produkt_taxonomien import GetProduktTaxonomien

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_produkt_taxonomien: Optional[GetProduktTaxonomien] = field(
            default=None,
            metadata={
                "name": "getProduktTaxonomien",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
