from dataclasses import dataclass, field
from typing import Optional

from ojp2.comparison_operator_enum import ComparisonOperatorEnum
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class HeaviestAxleWeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    heaviest_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    heaviest_axle_weight_characteristic_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "heaviestAxleWeightCharacteristicExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
