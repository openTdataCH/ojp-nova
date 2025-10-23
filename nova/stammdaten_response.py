from dataclasses import dataclass, field
from typing import List, Optional
from nova.abteil_art import AbteilArt
from nova.meldungen import Meldungen
from nova.partners import Partners
from nova.platz_lage import PlatzLage
from nova.stammdaten_erstattungs_bedingungen import StammdatenErstattungsBedingungen
from nova.stammdaten_haltestellen import StammdatenHaltestellen
from nova.stammdaten_kunden_segmente import StammdatenKundenSegmente
from nova.stammdaten_paket import StammdatenPaket
from nova.stammdaten_produkt_infos import StammdatenProduktInfos
from nova.stammdaten_zonen import StammdatenZonen
from nova.stammdaten_zonen_plaene import StammdatenZonenPlaene
from nova.stammdaten_zonen_tarife import StammdatenZonenTarife
from nova.verkaufs_parameter_typ import VerkaufsParameterTyp
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse
from nova.wagen_art import WagenArt
from nova.zone_stammdaten import ZoneStammdaten
from nova.zonen_plan import ZonenPlan
from nova.zonen_tarif import ZonenTarif

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenResponse(VertriebsStammdatenResponse):
    class Meta:
        name = "stammdatenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_paket: List[StammdatenPaket] = field(
        default_factory=list,
        metadata={
            "name": "stammdatenPaket",
            "type": "Element",
        }
    )
    stammdaten_haltestellen: Optional[StammdatenHaltestellen] = field(
        default=None,
        metadata={
            "name": "stammdatenHaltestellen",
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_zonen: Optional[StammdatenZonen] = field(
        default=None,
        metadata={
            "name": "stammdatenZonen",
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_produkt_infos: Optional[StammdatenProduktInfos] = field(
        default=None,
        metadata={
            "name": "stammdatenProduktInfos",
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_kunden_segmente: Optional[StammdatenKundenSegmente] = field(
        default=None,
        metadata={
            "name": "stammdatenKundenSegmente",
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_zonen_plaene: Optional[StammdatenZonenPlaene] = field(
        default=None,
        metadata={
            "name": "stammdatenZonenPlaene",
            "type": "Element",
            "required": True,
        }
    )
    partner: Optional[Partners] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_zonen_tarife: Optional[StammdatenZonenTarife] = field(
        default=None,
        metadata={
            "name": "stammdatenZonenTarife",
            "type": "Element",
            "required": True,
        }
    )
    stammdaten_erstattungs_bedingungen: Optional[StammdatenErstattungsBedingungen] = field(
        default=None,
        metadata={
            "name": "stammdatenErstattungsBedingungen",
            "type": "Element",
            "required": True,
        }
    )
    zone: List[ZoneStammdaten] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    zonen_plan: List[ZonenPlan] = field(
        default_factory=list,
        metadata={
            "name": "zonenPlan",
            "type": "Element",
        }
    )
    zonen_tarif: List[ZonenTarif] = field(
        default_factory=list,
        metadata={
            "name": "zonenTarif",
            "type": "Element",
        }
    )
    verkaufs_parameter: List[VerkaufsParameterTyp] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
        }
    )
    abteil_arte: List[AbteilArt] = field(
        default_factory=list,
        metadata={
            "name": "abteilArte",
            "type": "Element",
        }
    )
    wagen_arte: List[WagenArt] = field(
        default_factory=list,
        metadata={
            "name": "wagenArte",
            "type": "Element",
        }
    )
    platz_lagen: List[PlatzLage] = field(
        default_factory=list,
        metadata={
            "name": "platzLagen",
            "type": "Element",
        }
    )
    anfrage_protokoll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "anfrageProtokollId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
