from dataclasses import dataclass, field
from typing import Optional
from ojp.direction_enum import DirectionEnum
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.reference_point_direction_enum import ReferencePointDirectionEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadsideReferencePoint:
    roadside_reference_point_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    administrative_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    direction_bound: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBound",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    direction_relative: Optional[ReferencePointDirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionRelative",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    distance_from_previous: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceFromPrevious",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    distance_to_next: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceToNext",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    elevated_road_section: Optional[bool] = field(
        default=None,
        metadata={
            "name": "elevatedRoadSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    roadside_reference_point_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    roadside_reference_point_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    roadside_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
