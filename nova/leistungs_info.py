from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.klassen_typ_code import KlassenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsInfo:
    """Leistungen die nicht über die TKID definiert werden können (z.B.

    Abonnemente auf Sicherheitspapier), aber für die korrekte
    Tarifierung von Anschlussbilletten verwendet werden können.

    :ivar zonen_geltungs_bereich: Jede Leistung mit Zonegültigkeit hat
        i.d.R. einen zonenGeltungsBereich. Ausnahme: Gewisse
        Fahrausweise die in Zonen unterschiedlicher Verbunde gültig sind
        haben pro Verbund einen eigenen zonenGeltungsBereich.
    :ivar leistungs_info_id: Identifier der manuell angegebenen
        Leistung: kann entweder NOVA LeistungsID oder ein beliebiger
        anderer Identifier sein.
    :ivar gueltig_von:
    :ivar gueltig_bis:
    :ivar produkt_nummer:
    :ivar klasse:
    """
    zonen_geltungs_bereich: Optional["LeistungsInfo.ZonenGeltungsBereich"] = field(
        default=None,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_info_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsInfoId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
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
