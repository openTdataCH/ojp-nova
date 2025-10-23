from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.roadside_reference_point import RoadsideReferencePoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadsideReferencePointSecondaryLocation:
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    roadside_reference_point_secondary_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointSecondaryLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
