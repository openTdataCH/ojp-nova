from dataclasses import dataclass, field
from typing import List, Optional
from nova.freizeit_beleg_parameter import FreizeitBelegParameter
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FreizeitBelegRequest(VertriebsRequest):
    leistung: List["FreizeitBelegRequest.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
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
        beleg: List["FreizeitBelegRequest.Leistung.Beleg"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Beleg:
            beleg_parameter: List[FreizeitBelegParameter] = field(
                default_factory=list,
                metadata={
                    "name": "belegParameter",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            freizeit_traeger_medium_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "freizeitTraegerMediumCode",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                    "min_length": 0,
                    "max_length": 50,
                }
            )
