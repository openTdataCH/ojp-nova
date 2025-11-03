from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.roadside_reference_point_primary_location import (
    RoadsideReferencePointPrimaryLocation,
)
from ojp2.roadside_reference_point_secondary_location import (
    RoadsideReferencePointSecondaryLocation,
)

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadsideReferencePointLinear:
    roadside_reference_point_primary_location: Optional[
        RoadsideReferencePointPrimaryLocation
    ] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointPrimaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_secondary_location: Optional[
        RoadsideReferencePointSecondaryLocation
    ] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointSecondaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
