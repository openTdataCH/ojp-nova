from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.parkplatz import Parkplatz

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class MoeglicheParkplatz(Parkplatz):
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
