from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenFileResponse(VertriebsStammdatenResponse):
    """
    Die StammdatenFileAntwort dient als Container für Stammdatendatei-Pfad.
    """
    stammdaten_file_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "stammdatenFilePath",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 4000,
        }
    )
