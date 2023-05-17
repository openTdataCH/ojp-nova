from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class AusweisbarerZeitraum:
    """Ermöglicht die Angabe eines Zeitraum (von/bis) mit separater Angabe von
    Datum und Uhrzeit.

    Siehe auch Zeitraum, DatumZeitraum. Darf lediglich zu Ausgabezwecken
    (Druck / Screenanzeige) verwendet werden.
    """
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    von_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "vonZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    bis_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "bisZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
