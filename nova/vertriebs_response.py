from dataclasses import dataclass, field
from typing import Optional
from nova.meldungen import Meldungen

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsResponse:
    """
    :ivar meldungen:
    :ivar anfrage_protokoll_id:
    :ivar daten_release_id: Gibt die DatenRelease-ID an, die bei der
        Bearbeitung der Anfrage verwendet wurde.
    """
    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    anfrage_protokoll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "anfrageProtokollId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    daten_release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datenReleaseId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 100,
        }
    )
