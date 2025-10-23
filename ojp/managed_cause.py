from dataclasses import dataclass, field
from typing import Optional
from ojp.cause import Cause
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ManagedCause(Cause):
    managed_cause: Optional[str] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
