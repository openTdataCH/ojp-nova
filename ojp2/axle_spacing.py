from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AxleSpacing:
    axle_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    axle_spacing_sequence_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    axle_spacing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
