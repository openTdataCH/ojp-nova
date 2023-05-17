from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusRequestStructure(AbstractOjpserviceRequestStructure):
    class Meta:
        name = "OJPStatusRequestStructure"

    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
