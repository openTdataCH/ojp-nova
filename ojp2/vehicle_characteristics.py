from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.fuel_type_enum import FuelTypeEnum
from ojp2.gross_weight_characteristic import GrossWeightCharacteristic
from ojp2.heaviest_axle_weight_characteristic import (
    HeaviestAxleWeightCharacteristic,
)
from ojp2.height_characteristic import HeightCharacteristic
from ojp2.length_characteristic import LengthCharacteristic
from ojp2.load_type_enum import LoadTypeEnum
from ojp2.number_of_axles_characteristic import NumberOfAxlesCharacteristic
from ojp2.vehicle_equipment_enum import VehicleEquipmentEnum
from ojp2.vehicle_type_enum import VehicleTypeEnum
from ojp2.vehicle_usage_enum import VehicleUsageEnum
from ojp2.width_characteristic import WidthCharacteristic

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VehicleCharacteristics:
    fuel_type: Optional[FuelTypeEnum] = field(
        default=None,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    load_type: Optional[LoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "loadType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_equipment: Optional[VehicleEquipmentEnum] = field(
        default=None,
        metadata={
            "name": "vehicleEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_type: list[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_usage: Optional[VehicleUsageEnum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    gross_weight_characteristic: list[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    height_characteristic: list[HeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    length_characteristic: list[LengthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "lengthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    width_characteristic: list[WidthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "widthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    heaviest_axle_weight_characteristic: list[
        HeaviestAxleWeightCharacteristic
    ] = field(
        default_factory=list,
        metadata={
            "name": "heaviestAxleWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    number_of_axles_characteristic: list[NumberOfAxlesCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "numberOfAxlesCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    vehicle_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
