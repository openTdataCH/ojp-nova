from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.general_network_management_type_enum import GeneralNetworkManagementTypeEnum
from ojp.network_management import NetworkManagement
from ojp.person_category_enum import PersonCategoryEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GeneralNetworkManagement(NetworkManagement):
    general_network_management_type: Optional[GeneralNetworkManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    traffic_manually_directed_by: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "trafficManuallyDirectedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    general_network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
