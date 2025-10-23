from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.traffic_status_enum import TrafficStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ReferenceSettings:
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    traffic_status_default: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatusDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    reference_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "referenceSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
