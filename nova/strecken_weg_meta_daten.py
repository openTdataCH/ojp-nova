from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class StreckenWegMetaDaten:
    anzahl_verbindungen: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlVerbindungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999,
        }
    )
    mindest_anzahl_umstiege: Optional[int] = field(
        default=None,
        metadata={
            "name": "mindestAnzahlUmstiege",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 99,
        }
    )
    schnellste_reise_dauer: Optional[int] = field(
        default=None,
        metadata={
            "name": "schnellsteReiseDauer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999,
        }
    )
