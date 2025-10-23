from dataclasses import dataclass, field
from typing import Optional
from ojp.delays import Delays
from ojp.extension_type import ExtensionType
from ojp.traffic_constriction_type_enum import TrafficConstrictionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Impact:
    capacity_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacityRemaining",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    number_of_lanes_restricted: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLanesRestricted",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    number_of_operational_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfOperationalLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    original_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    residual_road_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualRoadWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    traffic_constriction_type: Optional[TrafficConstrictionTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficConstrictionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    delays: Optional[Delays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    impact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "impactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
