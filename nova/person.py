from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.geschlecht import Geschlecht
from nova.name_vorname import NameVorname
from nova.partner_1 import Partner1

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Person(Partner1):
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
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    geburts_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "geburtsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    geschlecht: Optional[Geschlecht] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    verstorben: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    version_geburts_datum: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionGeburtsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
