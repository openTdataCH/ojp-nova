from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_angebot import AbstractAngebot
from nova.angebot_bewertungs_info import AngebotBewertungsInfo
from nova.fahrt_wunsch_abdeckung import FahrtWunschAbdeckung
from nova.nutzungs_info import NutzungsInfo
from nova.produkt_einfluss_faktor_gruppe import ProduktEinflussFaktorGruppe
from nova.reise_gruppe_info import ReiseGruppeInfo
from nova.vertrags_info import VertragsInfo

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Angebot(AbstractAngebot):
    """
    Die Klasse repräsentiert ein Angebot, das von der öV-Plattform für eine
    Angebotsanfrage erzeugt wurde.
    """
    nutzungs_info: Optional[NutzungsInfo] = field(
        default=None,
        metadata={
            "name": "nutzungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zuschlags_angebot_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "zuschlagsAngebotRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
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
    geltungs_bereich_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "geltungsBereichRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    bewertungs_info: Optional[AngebotBewertungsInfo] = field(
        default=None,
        metadata={
            "name": "bewertungsInfo",
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
    bestehende_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "bestehendeLeistungsId",
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
    fahrt_wunsch_abdeckung: Optional[FahrtWunschAbdeckung] = field(
        default=None,
        metadata={
            "name": "fahrtWunschAbdeckung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fq_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "fqCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    nachtraegliche_einlieferung_moeglich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nachtraeglicheEinlieferungMoeglich",
            "type": "Attribute",
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
    kauf_erforderlich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kaufErforderlich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
