from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistung_verkaufs_parameter_type import LeistungVerkaufsParameterType
from nova.platz_vergabe_kriterien import PlatzVergabeKriterien

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsRequest:
    """
    Die Leistungsanfrage enthält alle Informationen, die notwendig sind, um für
    die übermittelte angebotsId eine Leistung offerieren zu können.

    :ivar verkaufs_parameter:
    :ivar platz_auswahl: obligatorisch und nur für Reservationsangebote
        gedacht
    :ivar angebots_id:
    :ivar externe_leistungs_referenz_id:
    :ivar externe_reisenden_referenz_id:
    :ivar leistungs_paket_id: Currently only implemented by NOVA FZ
        (Freizeit).
    :ivar angebots_paket_id: Currently only implemented by NOVA FZ
        (Freizeit).
    """
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    platz_auswahl: List["LeistungsRequest.PlatzAuswahl"] = field(
        default_factory=list,
        metadata={
            "name": "platzAuswahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
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
    angebots_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class PlatzAuswahl:
        """
        :ivar platz_vergabe_kriterien: Zonenauswahlkriterien für die
            automatische Platzwahl
        :ivar verbindungs_abschnitt_id:
        """
        platz_vergabe_kriterien: Optional[PlatzVergabeKriterien] = field(
            default=None,
            metadata={
                "name": "platzVergabeKriterien",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        verbindungs_abschnitt_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "verbindungsAbschnittId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
