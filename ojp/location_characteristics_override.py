from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.lane_enum import LaneEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class LocationCharacteristicsOverride:
    measurement_lanes_override: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "measurementLanesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    reversed_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reversedFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    location_characteristics_override_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverrideExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
