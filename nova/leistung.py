from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_leistung import AbstractLeistung
from nova.geltungs_bereich import GeltungsBereich
from nova.nutzungs_info import NutzungsInfo
from nova.produkt_einfluss_faktor_gruppe import ProduktEinflussFaktorGruppe
from nova.reise_gruppe_info import ReiseGruppeInfo
from nova.vertrags_info import VertragsInfo

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Leistung(AbstractLeistung):
    """Eine Leistung entsteht aus einem angebotenen Angebot.

    Eine Leistung wird in der Regel offeriert, Verkauft und
    anschliessend produziert.

    :ivar nutzungs_info:
    :ivar aktivierte_leistung:
    :ivar produkt_einfluss_faktoren:
    :ivar geltungs_bereich:
    :ivar reise_gruppen_info:
    :ivar vertrags_info: Information zum Vertrag in SAV
    :ivar enthaelt_swiss_pass_karte:
    :ivar benoetigt_neues_foto:
    """
    nutzungs_info: Optional[NutzungsInfo] = field(
        default=None,
        metadata={
            "name": "nutzungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    aktivierte_leistung: List["Leistung"] = field(
        default_factory=list,
        metadata={
            "name": "aktivierteLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_einfluss_faktoren: Optional[ProduktEinflussFaktorGruppe] = field(
        default=None,
        metadata={
            "name": "produktEinflussFaktoren",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    geltungs_bereich: Optional[GeltungsBereich] = field(
        default=None,
        metadata={
            "name": "geltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reise_gruppen_info: List[ReiseGruppeInfo] = field(
        default_factory=list,
        metadata={
            "name": "reiseGruppenInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_info: Optional[VertragsInfo] = field(
        default=None,
        metadata={
            "name": "vertragsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    enthaelt_swiss_pass_karte: bool = field(
        default=False,
        metadata={
            "name": "enthaeltSwissPassKarte",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    benoetigt_neues_foto: bool = field(
        default=False,
        metadata={
            "name": "benoetigtNeuesFoto",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
