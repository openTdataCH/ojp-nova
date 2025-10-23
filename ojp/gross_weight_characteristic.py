from dataclasses import dataclass, field
from typing import Optional
from ojp.comparison_operator_enum import ComparisonOperatorEnum
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GrossWeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
