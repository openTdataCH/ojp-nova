from dataclasses import dataclass, field
from typing import List, Optional
from nova.fahr_art_typ_code import FahrArtTypCode
from nova.geltungs_dauer_produkt_einfluss_faktor import GeltungsDauerProduktEinflussFaktor
from nova.generischer_produkt_einfluss_faktor import GenerischerProduktEinflussFaktor
from nova.klassen_typ_code import KlassenTypCode
from nova.kunden_segment_produkt_einfluss_faktor import KundenSegmentProduktEinflussFaktor

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ProduktEinflussFaktorGruppe:
    """
    ProdukteinflussfaktorGruppe beschreiben die unterschiedlichen Eigenschaften
    eines Angebots und dienen der flexiblen Bepreisung von Angeboten.
    """
    kunden_segment: Optional[KundenSegmentProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "kundenSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    geltungs_dauer: Optional[GeltungsDauerProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "geltungsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    generischer_einfluss_faktor: List[GenerischerProduktEinflussFaktor] = field(
        default_factory=list,
        metadata={
            "name": "generischerEinflussFaktor",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    fahr_art: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "name": "fahrArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
