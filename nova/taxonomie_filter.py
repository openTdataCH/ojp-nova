from dataclasses import dataclass, field
from typing import List, Optional
from nova.angebots_filter import AngebotsFilter
from nova.taxonomie_klasse_pfad import TaxonomieKlassePfad

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class TaxonomieFilter(AngebotsFilter):
    """
    Erlaubt die Filterung von Angeboten über Produkttaxonomien.

    :ivar produkt_taxonomie: Name der zu verwendenden Produkttaxonomie
    :ivar taxonomie_klasse_pfad: Geordnete Sequenz von Pfadangaben, mit
        der in der gewählten Produkttaxonomie die Taxonomieklassen
        ausgewählt werden, die dieser Filter anwenden soll. Beispiel:
        Die Sequenz ["Einzel", wildcard, "DV"] wählt alle
        Taxonomieklassen aus, die unterhalb "Einzel", dann irgend einer
        Klasse, dann "DV" liegen.
    """
    produkt_taxonomie: Optional[str] = field(
        default=None,
        metadata={
            "name": "produktTaxonomie",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    taxonomie_klasse_pfad: List[TaxonomieKlassePfad] = field(
        default_factory=list,
        metadata={
            "name": "taxonomieKlassePfad",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_occurs": 1,
        }
    )
