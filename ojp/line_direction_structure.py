from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineDirectionStructure:
    """
    Type for LINEand DIRECTION.

    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    """
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
