from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_2 import Extensions2
from ojp.line_direction_filter_structure import LineDirectionFilterStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationRequestStructure(AbstractOjpserviceRequestStructure):
    class Meta:
        name = "OJPLineInformationRequestStructure"

    line_direction_filter: Optional[LineDirectionFilterStructure] = field(
        default=None,
        metadata={
            "name": "LineDirectionFilter",
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
