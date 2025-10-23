from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ZoneStammdaten:
    """Repräsentiert eine Zone eines Tarifverbunds in der ein Ticket gültig ist.

    Zonen kommen bei der Tarifierung von Verbunds- und City-Tickets zur
    Anwendung. Eine Zone wird durch einen Code sowie passender
    Bezeichnung identifiziert.

    :ivar nachbar_zone_ref:
    :ivar zone_id:
    :ivar code:
    :ivar ist_lokal_netz:
    :ivar bezeichnung:
    :ivar zonen_owner: Partnercode des Zonen-Owners, d.h. des Verbunds,
        dem die Zone   gehört. Für  Zonen, die einem Zonenplan eines
        Verbunds wie Z-Pass/A-Welle zugeordnet sind, wird hier auf den
        Verbund ZVV bzw. A-Welle verwiesen.
    """
    nachbar_zone_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "nachbarZoneRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "tokens": True,
        }
    )
    zone_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "zoneId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    ist_lokal_netz: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istLokalNetz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 200,
        }
    )
    zonen_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "zonenOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 99999,
        }
    )
