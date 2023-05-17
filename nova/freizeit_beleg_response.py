from dataclasses import dataclass, field
from typing import List, Optional
from nova.ausgabe_status_typ import AusgabeStatusTyp
from nova.freizeit_beleg import FreizeitBeleg
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FreizeitBelegResponse(VertriebsResponse):
    """Die Belegantwort ist das Antwortsobjekt des 4.

    Klangs. Sie enthält für jede übermittelte LeistungId ein Objekt
    DruckDaten in dem alle zum Drucken notwendige Druckattribute
    enthalten sind.
    """
    leistung: List["FreizeitBelegResponse.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        ausgabe_status: Optional[AusgabeStatusTyp] = field(
            default=None,
            metadata={
                "name": "ausgabeStatus",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        beleg: List[FreizeitBeleg] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
