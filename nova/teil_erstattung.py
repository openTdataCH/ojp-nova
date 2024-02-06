from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class TeilErstattung:
    """Das Objekt Teilerstattung kann Teil einer ErstattungsAngebotsanfrage sein.
    Eine Teilerstattung enthält (optional) Informationen zu:

    - der Anzahl benutzter Einheiten Leistung der ErstattungsAngebotsanfrage - dem gewünschten Erstattungsdatum
    """
    letztes_gueltigkeits_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "letztesGueltigkeitsDatum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    anzahl_genutzte_einheiten: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlGenutzteEinheiten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999,
        }
    )
    angebot_id_benutzter_teil: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotIdBenutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
