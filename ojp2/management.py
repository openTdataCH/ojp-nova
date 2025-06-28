from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.filter_exit_management import FilterExitManagement
from ojp2.life_cycle_management import LifeCycleManagement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Management:
    life_cycle_management: Optional[LifeCycleManagement] = field(
        default=None,
        metadata={
            "name": "lifeCycleManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_exit_management: Optional[FilterExitManagement] = field(
        default=None,
        metadata={
            "name": "filterExitManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
