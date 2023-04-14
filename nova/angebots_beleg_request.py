from dataclasses import dataclass, field
from typing import List
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsBelegRequest(VertriebsRequest):
    """
    Das Objekt Beleganfrage dient als Container für alle Informationen, die
    notwendig sind, um für die übermittelten angebotsId eine
    AngebotsBelegantwort zu liefern.
    """
    angebots_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
