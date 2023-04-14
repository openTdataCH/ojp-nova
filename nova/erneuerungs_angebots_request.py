from dataclasses import dataclass, field
from typing import List
from nova.erneuerungs_request import ErneuerungsRequest
from nova.savangebots_request import SavangebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErneuerungsAngebotsRequest(SavangebotsRequest):
    """Die ErneuerungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Ihr wird nebst der leistungsID oder leistungsReferenz ein gültigAb
    Datum mitgegeben, ab wann die zu erneuernde Leistung gültig sein
    soll. Im Falle von personalisierten Angeboten enthält sie zudem
    einen Reisenden. Siehe auch SAVAngebotsAnfrage.
    """
    erneuerungs_request: List[ErneuerungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "erneuerungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
