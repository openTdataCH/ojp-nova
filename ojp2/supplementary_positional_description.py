from dataclasses import dataclass, field
from typing import Optional

from ojp2.carriageway_enum import CarriagewayEnum
from ojp2.extension_type import ExtensionType
from ojp2.lane_enum import LaneEnum
from ojp2.location_descriptor_enum import LocationDescriptorEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class SupplementaryPositionalDescription:
    carriageway: list[CarriagewayEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    footpath: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    lane: list[LaneEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    length_affected: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthAffected",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_descriptor: list[LocationDescriptorEnum] = field(
        default_factory=list,
        metadata={
            "name": "locationDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "locationPrecision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sequential_ramp_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequentialRampNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "supplementaryPositionalDescriptionExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
