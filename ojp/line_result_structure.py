from dataclasses import dataclass, field
from typing import List, Optional
from ojp.area_structure import AreaStructure
from ojp.linear_shape_structure import LinearShapeStructure
from ojp.mode_structure import ModeStructure
from ojp.ojperror_structure import OjperrorStructure
from ojp.published_line_name import PublishedLineName

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
        multiple ROUTEs and each has its own geometry. The first should
        be the "main" geometry.
    :ivar area_geometry: The LINE's main area. Used for MOBILITY
        SERVICES that cover one or more areas. The interconnection
        between the areas is not calculated (e.g. exclusion zones can't
        be modelled). Don't mix RouteGeometry and AreaGeometry in a
        response.
    :ivar mode: List of transport modes that are supported by this line.
    """
    error_condition: List[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    published_line_name: Optional[PublishedLineName] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    route_geometry: List[LinearShapeStructure] = field(
        default_factory=list,
        metadata={
            "name": "RouteGeometry",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    area_geometry: List[AreaStructure] = field(
        default_factory=list,
        metadata={
            "name": "AreaGeometry",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    mode: List[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
