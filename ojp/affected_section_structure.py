from dataclasses import dataclass, field
from typing import Optional
from ojp.extensions_1 import Extensions1
from ojp.link_projection_structure import LinkProjectionStructure
from ojp.offset_structure import OffsetStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedSectionStructure:
    """
    Type for information about the sectons affected by a SITUATION.

    :ivar section_ref: Reference to a section of ROUTE affected by a
        SITUATION.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """
    section_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
