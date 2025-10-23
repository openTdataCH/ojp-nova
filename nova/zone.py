from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Zone:
    """Repräsentiert eine Zone eines Tarifverbunds in der ein Ticket gültig ist.

    Zonen kommen bei der Tarifierung von Verbunds- und City-Tickets zur
    Anwendung. Eine Zone wird durch einen Code sowie passender
    Bezeichnung identifiziert.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    ist_lokalnetz: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istLokalnetz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zonen_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "zonenOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
