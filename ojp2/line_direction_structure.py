from dataclasses import dataclass, field
from typing import Optional

from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineDirectionStructure:
    """
    Type for LINEand DIRECTION.

    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    """

    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
