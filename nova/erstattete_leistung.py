from dataclasses import dataclass, field
from typing import List, Optional
from nova.erstattungs_daten import ErstattungsDaten
from nova.preis import Preis
from nova.zahlungs_information import ZahlungsInformation

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstatteteLeistung:
    original_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "originalPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattungs_daten: Optional[ErstattungsDaten] = field(
        default=None,
        metadata={
            "name": "erstattungsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zahlungs_information: List[ZahlungsInformation] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
