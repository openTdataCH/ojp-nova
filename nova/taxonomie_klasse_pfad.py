from dataclasses import dataclass, field
from typing import Optional
from nova.empty_type import EmptyType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class TaxonomieKlassePfad:
    """
    :ivar wildcard: Leeres XML-Element. Anzugeben, um auf der
        vorliegenden Ebene jeden Klassennamen zu matchen (a.k.a. "*").
    :ivar klassen_name: Name der Taxonomieklasse, der auf der
        vorliegenden Ebene gematcht wird.
    """
    wildcard: Optional[EmptyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    klassen_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "klassenName",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )
