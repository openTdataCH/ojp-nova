from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class TarifStufe:
    """Die Tarifstufe gibt die Anzahl Zonen an, die für die Preisberechnung
    zugrunde gelegt wurden.

    Die Anzahl der Zonen aus der Tarifstufe deckt sich nicht zwingend
    mit der Anzahl der Zonen, die tatsächlich befahren werden dürfen.
    Eine Tarifstufe kann aber auch "Alle Zonen" oder "Kurzstrecke" sein.
    """
    tarif_stufen_text: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "tarifStufenText",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    anzahl_tarifierte_zonen: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlTarifierteZonen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_stufen_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "tarifStufenCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
