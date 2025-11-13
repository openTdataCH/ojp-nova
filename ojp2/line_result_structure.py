from dataclasses import dataclass, field
from typing import Optional

from ojp2.area_structure import AreaStructure
from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.line_ref_structure import LineRefStructure
from ojp2.linear_shape_structure import LinearShapeStructure
from ojp2.mode_structure import ModeStructure
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.published_line_name import PublishedLineName

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LineResultStructure:
    """
    :ivar error_condition: Problems related to this Line result.
    :ivar line_ref: Reference to the LINE.
    :ivar published_line_name: Name or Number by which the LINE is known
        to the public.
    :ivar direction_ref: DIRECTION of LINE.
    :ivar route_geometry: The LINE's route geometry. A line can have
        multiple ROUTEs, and each has its own geometry. The first should
        be the "main" geometry.
    :ivar area_geometry: The LINE's main area. Used for MOBILITY
        SERVICES that cover one or more areas. The interconnection
        between the areas is not calculated (e.g., exclusion zones can't
        be modelled). Don't mix RouteGeometry and AreaGeometry in a
        response.
    :ivar mode: List of transport modes that are supported by this line.
    """

    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    published_line_name: Optional[PublishedLineName] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    route_geometry: list[LinearShapeStructure] = field(
        default_factory=list,
        metadata={
            "name": "RouteGeometry",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    area_geometry: list[AreaStructure] = field(
        default_factory=list,
        metadata={
            "name": "AreaGeometry",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    mode: list[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
