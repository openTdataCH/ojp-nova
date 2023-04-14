from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_loc03_other_point_descriptor_subtype_enum import TpegLoc03OtherPointDescriptorSubtypeEnum
from ojp.tpeg_point_descriptor import TpegPointDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegOtherPointDescriptor(TpegPointDescriptor):
    tpeg_other_point_descriptor_type: Optional[TpegLoc03OtherPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_other_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
