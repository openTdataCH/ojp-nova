from dataclasses import dataclass, field
from typing import List, Optional
from ojp.compliance_option_enum import ComplianceOptionEnum
from ojp.direction_enum import DirectionEnum
from ojp.extension_type import ExtensionType
from ojp.operator_action import OperatorAction
from ojp.places_enum import PlacesEnum
from ojp.traffic_type_enum import TrafficTypeEnum
from ojp.vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class NetworkManagement(OperatorAction):
    compliance_option: Optional[ComplianceOptionEnum] = field(
        default=None,
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    applicable_for_traffic_direction: List[DirectionEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    applicable_for_traffic_type: List[TrafficTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    places_at_which_applicable: List[PlacesEnum] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    automatically_initiated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
