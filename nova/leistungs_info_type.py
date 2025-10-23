from dataclasses import dataclass, field
from typing import List, Optional
from nova.klassen_typ_code import KlassenTypCode
from nova.zeitraum import Zeitraum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsInfoType:
    """
    Leistung die an ein Anschlussbillett angerechnet wurde.

    :ivar leistungs_id: Identifier einer NOVA-Leistung.
    :ivar externe_leistungs_referenz_id: Identifier einer Leistung die
        nicht über NOVA verkauft wurde.
    :ivar gueltigkeit:
    :ivar zonen_geltungs_bereich: Jede Leistung mit Zonegültigkeit hat
        i.d.R. einen zonenGeltungsBereich. Ausnahme: Gewisse
        Fahrausweise die in Zonen unterschiedlicher Verbunde gültig sind
        haben pro Verbund einen eigenen zonenGeltungsBereich.
    :ivar tarif_owner:
    :ivar produkt_nummer:
    :ivar klasse:
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    gueltigkeit: List[Zeitraum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zonen_geltungs_bereich: List["LeistungsInfoType.ZonenGeltungsBereich"] = field(
        default_factory=list,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class ZonenGeltungsBereich:
        zone: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
        alle_zonen: Optional[bool] = field(
            default=None,
            metadata={
                "name": "alleZonen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
