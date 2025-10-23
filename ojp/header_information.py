from dataclasses import dataclass, field
from typing import Optional
from ojp.area_of_interest_enum import AreaOfInterestEnum
from ojp.confidentiality_value_enum import ConfidentialityValueEnum
from ojp.extension_type import ExtensionType
from ojp.information_status_enum import InformationStatusEnum
from ojp.urgency_enum import UrgencyEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class HeaderInformation:
    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "areaOfInterest",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    confidentiality: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    information_status: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    urgency: Optional[UrgencyEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
