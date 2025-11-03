from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.line_result_structure import LineResultStructure
from ojp2.ojpline_information_request import OjplineInformationRequest

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
        },
    )
    line_result: list[LineResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
