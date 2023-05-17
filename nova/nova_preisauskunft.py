from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.nova_base import (
    ClientIdentifier,
    CorrelationKontext,
    GeldBetrag,
    Meldungen,
    TimeShift,
)
from nova.nova_vertriebs_base import (
    AngebotsFilter,
    ReisendenTypCode,
)
from nova.nova_vertriebsservice import (
    FahrplanVerbindungsSegment,
    GueltigkeitsZeitraum,
    ProduktEinflussFaktorGruppe,
)

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class PreisAuspraegung:
    produkt_einfluss_faktoren: Optional[ProduktEinflussFaktorGruppe] = field(
        default=None,
        metadata={
            "name": "produktEinflussFaktoren",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
    preis: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    nutzungs_zeitraum: Optional[GueltigkeitsZeitraum] = field(
        default=None,
        metadata={
            "name": "nutzungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzID",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_length": 0,
            "max_length": 50,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verfuegbares_kontingent: Optional[int] = field(
        default=None,
        metadata={
            "name": "verfuegbaresKontingent",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )


@dataclass
class ReisendenInfoPreisAuskunft:
    ermaessigungs_karte_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ermaessigungsKarteCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_length": 0,
            "max_length": 50,
        }
    )
    alter: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 200,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    reisenden_typ: Optional[ReisendenTypCode] = field(
        default=None,
        metadata={
            "name": "reisendenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )


@dataclass
class VerbindungPreisAuskunft:
    segment_hin_fahrt: List[FahrplanVerbindungsSegment] = field(
        default_factory=list,
        metadata={
            "name": "segmentHinFahrt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class PreisAuskunftRequest:
    """
    Abstrakte Basisklasse für ProduktPreisAuskunft und VerbindungPreisAuskunft.
    """
    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    time_shift: Optional[TimeShift] = field(
        default=None,
        metadata={
            "name": "timeShift",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    reisender: List[ReisendenInfoPreisAuskunft] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    kunden_segmente_gruppieren: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kundenSegmenteGruppieren",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )


@dataclass
class PreisAuskunftResponse:
    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    preis_auspraegung: List[PreisAuspraegung] = field(
        default_factory=list,
        metadata={
            "name": "preisAuspraegung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )


@dataclass
class ProduktPreisAuskunftRequest(PreisAuskunftRequest):
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )


@dataclass
class VerbindungPreisAuskunftRequest(PreisAuskunftRequest):
    verbindung: List[VerbindungPreisAuskunft] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )


@dataclass
class ErstellePreisAuskunft:
    class Meta:
        name = "erstellePreisAuskunft"
        namespace = "http://nova.voev.ch/services/v14/preisauskunft"

    preis_auskunft_request: Optional[PreisAuskunftRequest] = field(
        default=None,
        metadata={
            "name": "PreisAuskunftRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstellePreisAuskunftResponse:
    class Meta:
        name = "erstellePreisAuskunftResponse"
        namespace = "http://nova.voev.ch/services/v14/preisauskunft"

    preis_auskunft_response: Optional[PreisAuskunftResponse] = field(
        default=None,
        metadata={
            "name": "preisAuskunftResponse",
            "type": "Element",
            "required": True,
        }
    )
