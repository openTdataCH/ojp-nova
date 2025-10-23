from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.klassen_typ_code import KlassenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbundLeistungsInfo:
    """
    :ivar leistungs_id: @Deprecated Wird in NOVA 15 entfernt. Bitte das
        Element verbundLeistung befüllen.
    :ivar verbund_leistung:
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
    verbund_leistung: Optional["VerbundLeistungsInfo.VerbundLeistung"] = field(
        default=None,
        metadata={
            "name": "verbundLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class VerbundLeistung:
        """Verbund-Leistung die nicht mit einer TKID verknüpft ist (z.B.

        Abonnement auf Sicherheitspapier), aber für die korrekte
        Tarifierung von Anschlussbilletten verwendet werden kann.
        """
        verbund_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "verbundCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "max_inclusive": 99999,
            }
        )
        produkt_nummer: Optional[int] = field(
            default=None,
            metadata={
                "name": "produktNummer",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_inclusive": 0,
            }
        )
        zonen_geltungs_bereich: Optional["VerbundLeistungsInfo.VerbundLeistung.ZonenGeltungsBereich"] = field(
            default=None,
            metadata={
                "name": "zonenGeltungsBereich",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        externe_leistungs_referenz_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "externeLeistungsReferenzId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
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
