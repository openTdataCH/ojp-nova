from dataclasses import dataclass, field
from typing import List, Optional
from nova.oev_anfrage_parameter_type import OevAnfrageParameterType
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FreizeitKombinationAngebotsRequest(VertriebsRequest):
    oev_anfrage_parameter: Optional[OevAnfrageParameterType] = field(
        default=None,
        metadata={
            "name": "oevAnfrageParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    freizeit_angebot: List["FreizeitKombinationAngebotsRequest.FreizeitAngebot"] = field(
        default_factory=list,
        metadata={
            "name": "freizeitAngebot",
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
    class FreizeitAngebot:
        freizeit_angebots_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "freizeitAngebotsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        oev_reisender_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "oevReisenderRef",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
