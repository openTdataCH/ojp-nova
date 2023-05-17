from dataclasses import dataclass, field
from typing import List
from nova.angebots_druck_daten import AngebotsDruckDaten
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsBelegResponse(VertriebsResponse):
    """Die AngebotsBelegantwort ist das Antwortsobjekt fuer
    liefereBelegeFuerAngebot.

    Sie enthält für jede übermittelte AngebotsId ein Objekt
    AngebotsDruckDaten in dem alle bereits für das Angebot vorliegenden
    Druckattribute enthalten sind. Dies sind u.U. nicht alle
    Druckattribute (z.B. Sicherheitselement, LeistungsId, Zahlmittel
    fehlen).
    """
    angebots_druck_daten: List[AngebotsDruckDaten] = field(
        default_factory=list,
        metadata={
            "name": "angebotsDruckDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
