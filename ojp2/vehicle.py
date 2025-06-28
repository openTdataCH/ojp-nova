from dataclasses import dataclass, field
from typing import Optional

from ojp2.axle_spacing import AxleSpacing
from ojp2.axle_weight import AxleWeight
from ojp2.extension_type import ExtensionType
from ojp2.hazardous_materials import HazardousMaterials
from ojp2.multilingual_string import MultilingualString
from ojp2.vehicle_characteristics import VehicleCharacteristics
from ojp2.vehicle_status_enum import VehicleStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Vehicle:
    vehicle_colour: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_country_of_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleCountryOfOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleManufacturer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_registration_plate_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleRegistrationPlateIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    axle_spacing_on_vehicle: list[AxleSpacing] = field(
        default_factory=list,
        metadata={
            "name": "axleSpacingOnVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_axle_weight: list[AxleWeight] = field(
        default_factory=list,
        metadata={
            "name": "specificAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazardous_goods_associated_with_vehicle: Optional[HazardousMaterials] = (
        field(
            default=None,
            metadata={
                "name": "hazardousGoodsAssociatedWithVehicle",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
    vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
