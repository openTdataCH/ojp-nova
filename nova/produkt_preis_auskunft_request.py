from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.preis_auskunft_request import PreisAuskunftRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class ProduktPreisAuskunftRequest(PreisAuskunftRequest):
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
