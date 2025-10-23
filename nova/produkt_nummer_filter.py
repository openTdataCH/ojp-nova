from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_filter import AngebotsFilter

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ProduktNummerFilter(AngebotsFilter):
    """
    Ein Angebotsfilter, der ein Produkt eindeutig identifiziert.
    """
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )
