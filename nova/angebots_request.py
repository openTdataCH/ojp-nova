from dataclasses import dataclass, field
from typing import List, Optional
from nova.angebots_filter import AngebotsFilter
from nova.gruppen_reise_info_request import GruppenReiseInfoRequest
from nova.klassen_typ_code import KlassenTypCode
from nova.rabatt_anfrage_type import RabattAnfrageType
from nova.reisenden_info import ReisendenInfo
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsRequest(VertriebsRequest):
    """Die Klasse AngebotsRequest ist die abstrakte Basisklasse für alle Strecken-,
    Zonen- und produktbasierten Angebotsanfragen.

    Die Angebotsanfrage ihrerseits ist eine Subklasse einer
    Vertriebsanfrage.

    :ivar traeger_medium:
    :ivar reisender:
    :ivar gruppen_reise_info:
    :ivar angebots_filter:
    :ivar klasse:
    :ivar rabatt_request:
    :ivar kunden_segmente_gruppieren: Wenn true, werden falls moeglich
        Angebote fuer eine KundenSegmentgruppe (z.B. ERMAESSIGT) statt
        Einzel-KundenSegmente (z.B. KIND_6-16, HALBTAX etc.) geliefert.
        Insbesondere bei Angebotsanfragen ohne ReisendenInfo wird
        dadurch die Angebotsmenge stark reduziert.
    :ivar vertrags_partner:
    :ivar basis_vertrags_nummer:
    """
    traeger_medium: List[str] = field(
        default_factory=list,
        metadata={
            "name": "traegerMedium",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    reisender: List[ReisendenInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gruppen_reise_info: List[GruppenReiseInfoRequest] = field(
        default_factory=list,
        metadata={
            "name": "gruppenReiseInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    klasse: List[KlassenTypCode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rabatt_request: Optional[RabattAnfrageType] = field(
        default=None,
        metadata={
            "name": "rabattRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    kunden_segmente_gruppieren: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kundenSegmenteGruppieren",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    vertrags_partner: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsPartner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    basis_vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "basisVertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
