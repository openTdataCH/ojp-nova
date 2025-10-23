from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_leistung import AbstractLeistung
from nova.erstattete_leistung import ErstatteteLeistung
from nova.geld_betrag import GeldBetrag

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Savleistung(AbstractLeistung):
    """
    :ivar total_erstattungs_betraege:
    :ivar erstattete_leistung:
    :ivar erstattungs_begruendung:
    :ivar selbst_behalt:
    :ivar traeger_medium: Momentan konstant "SICHERHEITSPAPIER"
    """
    class Meta:
        name = "SAVLeistung"

    total_erstattungs_betraege: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "totalErstattungsBetraege",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattete_leistung: List[ErstatteteLeistung] = field(
        default_factory=list,
        metadata={
            "name": "erstatteteLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    erstattungs_begruendung: Optional[str] = field(
        default=None,
        metadata={
            "name": "erstattungsBegruendung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    selbst_behalt: Optional[str] = field(
        default=None,
        metadata={
            "name": "selbstBehalt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "total_digits": 12,
            "fraction_digits": 2,
            "pattern": r"-?[0-9]{1,10}(\.[0-9]{0,2})?",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
