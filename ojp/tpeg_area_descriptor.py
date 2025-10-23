from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_descriptor import TpegDescriptor
from ojp.tpeg_loc03_area_descriptor_subtype_enum import TpegLoc03AreaDescriptorSubtypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegAreaDescriptor(TpegDescriptor):
    tpeg_area_descriptor_type: Optional[TpegLoc03AreaDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_area_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
