from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_area_descriptor import TpegAreaDescriptor
from ojp.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegNamedOnlyArea(TpegAreaLocation):
    name: List[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    tpeg_named_only_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
