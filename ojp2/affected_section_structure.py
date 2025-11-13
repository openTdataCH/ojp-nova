from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.link_projection_structure import LinkProjectionStructure
from ojp2.offset_structure import OffsetStructure
from ojp2.quay_ref_structure_2 import QuayRefStructure2
from ojp2.section_ref_structure import SectionRefStructure
from ojp2.stop_place_ref_structure_1 import StopPlaceRefStructure1
from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedSectionStructure:
    """
    Type for information about the SECTIONs affected by a SITUATION.

    :ivar section_ref: Reference to a section of ROUTE affected by a
        SITUATION.
    :ivar indirect_section_ref: An indirect reference to a COMMON
        SECTION by stating the stop point ref of the first and last
        POINT IN JOURNEY PATTERN of the section in question.
        Intermediate POINTs should be added if necessary to distinguish
        different sections having the same start and end point and is a
        means to exclude sections not containing those stop points.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """

    section_ref: Optional[SectionRefStructure] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    indirect_section_ref: Optional[
        "AffectedSectionStructure.IndirectSectionRef"
    ] = field(
        default=None,
        metadata={
            "name": "IndirectSectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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

    @dataclass
    class IndirectSectionRef:
        """
        :ivar first_stop_point_ref: Used to indicate the SCHEDULED stop
            point at the start of the SECTION
        :ivar first_stop_place_ref: Used to indicate that any SCHEDULED
            stop point with a stop assignment to the indicated StopPlace
            is to be considered as start of the SECTION
        :ivar first_quay_ref: Used to indicate that any SCHEDULED stop
            point with a stop assignment to the indicated QUAY is to be
            considered as start of the SECTION
        :ivar intermediate_stop_point_ref: An intermediate Stop POINT of
            the SECTION that must be part of SECTION
        :ivar intermediate_stop_place_ref: Used to indicate that at
            least one SCHEDULED stop point with a stop assignment to the
            indicated StopPlace must be part of the SECTION
        :ivar intermediate_quay_ref: Used to indicate that at least one
            SCHEDULED stop point with a stop assignment to the indicated
            QUAY must be part of the SECTION
        :ivar last_stop_point_ref: Used to indicate the SCHEDULED stop
            point at the end of the SECTION
        :ivar last_stop_place_ref: Used to indicate that any SCHEDULED
            stop point with a stop assignment to the indicated StopPlace
            is to be considered as end of the SECTION
        :ivar last_quay_ref: Used to indicate that any SCHEDULED stop
            point with a stop assignment to the indicated QUAY is to be
            considered as end of the SECTION
        """

        first_stop_point_ref: Optional[StopPointRefStructure] = field(
            default=None,
            metadata={
                "name": "FirstStopPointRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        first_stop_place_ref: Optional[StopPlaceRefStructure1] = field(
            default=None,
            metadata={
                "name": "FirstStopPlaceRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        first_quay_ref: Optional[QuayRefStructure2] = field(
            default=None,
            metadata={
                "name": "FirstQuayRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        intermediate_stop_point_ref: list[StopPointRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "IntermediateStopPointRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        intermediate_stop_place_ref: list[StopPlaceRefStructure1] = field(
            default_factory=list,
            metadata={
                "name": "IntermediateStopPlaceRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        intermediate_quay_ref: list[QuayRefStructure2] = field(
            default_factory=list,
            metadata={
                "name": "IntermediateQuayRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        last_stop_point_ref: Optional[StopPointRefStructure] = field(
            default=None,
            metadata={
                "name": "LastStopPointRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        last_stop_place_ref: Optional[StopPlaceRefStructure1] = field(
            default=None,
            metadata={
                "name": "LastStopPlaceRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        last_quay_ref: Optional[QuayRefStructure2] = field(
            default=None,
            metadata={
                "name": "LastQuayRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
