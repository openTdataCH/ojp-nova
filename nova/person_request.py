from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.geschlecht import Geschlecht
from nova.name_vorname import NameVorname
from nova.partner_request import PartnerRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class PersonRequest(PartnerRequest):
    name: Optional[NameVorname] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    titel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    geburts_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "geburtsDatum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    geschlecht: Optional[Geschlecht] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    verstorben: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
