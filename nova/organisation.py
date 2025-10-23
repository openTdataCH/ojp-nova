from dataclasses import dataclass, field
from typing import Optional
from nova.name_vorname import NameVorname
from nova.partner_1 import Partner1

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Organisation(Partner1):
    ansprech_partner: Optional[NameVorname] = field(
        default=None,
        metadata={
            "name": "ansprechPartner",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    organisation1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    organisation2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    version_organisation: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionOrganisation",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
