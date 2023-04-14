from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_2 import Extensions2
from ojp.line_result_structure import LineResultStructure
from ojp.ojpline_information_request import OjplineInformationRequest

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationDeliveryStructure(AbstractServiceDeliveryStructure):
    class Meta:
        name = "OJPLineInformationDeliveryStructure"

    ojpline_information_request: Optional[OjplineInformationRequest] = field(
        default=None,
        metadata={
            "name": "OJPLineInformationRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    line_result: List[LineResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
