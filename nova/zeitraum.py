from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Zeitraum:
    """Ermöglicht die Angabe eines Zeitraum (von/bis) mit Uhrzeit.

    Siehe auch DatumZeitraum, AusweisbarerZeitraum.
    """
    von: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
