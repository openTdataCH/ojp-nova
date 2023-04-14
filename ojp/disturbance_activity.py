from dataclasses import dataclass, field
from typing import Optional
from ojp.activity import Activity
from ojp.disturbance_activity_type_enum import DisturbanceActivityTypeEnum
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class DisturbanceActivity(Activity):
    disturbance_activity_type: Optional[DisturbanceActivityTypeEnum] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    disturbance_activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
