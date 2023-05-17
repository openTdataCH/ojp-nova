from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.savangebots_request import SavangebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class HinterlegungsAngebotsRequest(SavangebotsRequest):
    vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 10,
        }
    )
    hinterlegung_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "hinterlegungVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    hinterlegung_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "hinterlegungBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
