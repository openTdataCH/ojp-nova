from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationVersion:
    """Type for SITUATION version number if entry is update to a previous version.

    Unique within IncidentNumber. Monotonically increasing within
    IncidentNumber. Any values for classification, description, affects,
    effects that are present in an update replace any values on previous
    incidents and updates with the same identifier. Values that are not
    updated remain in effect.
    """

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
