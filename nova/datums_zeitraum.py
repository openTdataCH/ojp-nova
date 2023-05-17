from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class DatumsZeitraum:
    """Ermöglicht die Angabe eines Datumszeitraum (von/bis) ohne Uhrzeit.

    Siehe auch Zeitraum, AusweisbarerZeitraum.
    """
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
