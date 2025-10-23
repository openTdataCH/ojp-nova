from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.lokal_netze import LokalNetze
from nova.verbund_strecken import VerbundStrecken

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class HaltestellenVerbundDaten:
    """
    Verbundspezifische Daten (Lokalnetze und Spezialstrecken) zur angefragten
    Haltestelle.
    """
    lokal_netze: Optional[LokalNetze] = field(
        default=None,
        metadata={
            "name": "lokalNetze",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    verbund_strecken: Optional[VerbundStrecken] = field(
        default=None,
        metadata={
            "name": "verbundStrecken",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
