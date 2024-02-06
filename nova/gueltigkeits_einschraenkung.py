from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.gueltigkeits_einschraenkung_typ import GueltigkeitsEinschraenkungTyp
from nova.uhrzeit_abschnitt import UhrzeitAbschnitt
from nova.wochen_tag import WochenTag

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GueltigkeitsEinschraenkung:
    kalender_tag: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "kalenderTag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    wochen_tag: List[WochenTag] = field(
        default_factory=list,
        metadata={
            "name": "wochenTag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    uhrzeit_abschnitt: Optional[UhrzeitAbschnitt] = field(
        default=None,
        metadata={
            "name": "uhrzeitAbschnitt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    typ: Optional[GueltigkeitsEinschraenkungTyp] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
