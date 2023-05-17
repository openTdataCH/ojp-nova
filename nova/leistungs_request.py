from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistung_verkaufs_parameter_type import LeistungVerkaufsParameterType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsRequest:
    """
    Die Leistungsanfrage enthält alle Informationen, die notwendig sind, um für die
    übermittelte angebotsId eine Leistung offerieren zu können.

    :ivar verkaufs_parameter:
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
