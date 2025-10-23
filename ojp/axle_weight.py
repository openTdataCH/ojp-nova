from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AxleWeight:
    axle_position_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axlePositionIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    maximum_permitted_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumPermittedAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    axle_weight_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleWeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
