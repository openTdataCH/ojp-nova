from dataclasses import dataclass, field
from typing import List, Optional
from nova.operator import Operator

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsSucheFeld:
    """@Deprecated Will be removed in NOVA 15.

    :ivar such_begriff: Suchbegriff, nach welchem im Feldname gesucht
        wird. Werden mehrere Suchbegriffe angegeben, so werden diese
        ODER-verknüpft. Hinweis: Datum/Zeit-Werte werden als String
        analog zum Format xs:dateTime angegeben.
    :ivar key: Schlüssel des Leistungs-Feldes, welches durchsucht werden
        soll. Hinweis: die möglichen Keys werden in einer separaten
        Liste publiziert.
    :ivar operator: Definiert, wie im Feld nach dem Suchbegriff gesucht
        wird (z.B. gleich, grösser oder gleich, kleiner oder gleich).
    """
    such_begriff: List[str] = field(
        default_factory=list,
        metadata={
            "name": "suchBegriff",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    operator: Optional[Operator] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
