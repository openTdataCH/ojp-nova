from dataclasses import dataclass, field
from typing import Optional
from nova.name_vorname import NameVorname
from nova.partner_request import PartnerRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class OrganisationRequest(PartnerRequest):
    organisation1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    organisation2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    ansprech_partner: Optional[NameVorname] = field(
        default=None,
        metadata={
            "name": "ansprechPartner",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
