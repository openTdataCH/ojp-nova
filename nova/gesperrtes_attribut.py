from dataclasses import dataclass, field
from typing import Optional
from nova.partner_attribut import PartnerAttribut

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class GesperrtesAttribut:
    gesperrt: Optional[PartnerAttribut] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
