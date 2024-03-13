from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class TkidZusammenfuehrung:
    """
    :ivar referenzierte_tkid: TKID, welche fortan von der
        referenzierendenTkid referenziert werden soll.
    :ivar referenzierende_tkid: TKID, welche die referenzierteTkid
        fortan referenzieren soll.
    """
    referenzierte_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenzierteTkid",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    referenzierende_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenzierendeTkid",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
