from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsFachSchluessel:
    """
    :ivar leistungs_id:
    :ivar leistungs_referenz:
    :ivar sicherheits_element_id: ID, wie vom SicherheitselementService
        vergeben.
    :ivar leistungs_paket_id:
    :ivar erneuerungs_id: UUID der Leistung, die in der URL im
        ErneurungsInfoService verwendet wird
    :ivar kunden_name:
    :ivar kunden_vorname:
    :ivar kunden_geburts_datum:
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
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sicherheits_element_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "sicherheitsElementId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 20,
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
    erneuerungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "erneuerungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    kunden_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 30,
        }
    )
    kunden_vorname: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenVorname",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 30,
        }
    )
    kunden_geburts_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "kundenGeburtsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
