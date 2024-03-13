from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsStammdatenResponse:
    """
    Liefert die DatenRelease- und Vertriebskonfiguration-ID die auf Basis der
    VertriebsstammdatenAnfrage ermittelt wurden.
    """
    daten_release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datenReleaseId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 100,
        }
    )
    vertriebs_konfiguration_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertriebsKonfigurationId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 255,
        }
    )
