from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.tpeg_descriptor import TpegDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegPointDescriptor(TpegDescriptor):
    tpeg_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
