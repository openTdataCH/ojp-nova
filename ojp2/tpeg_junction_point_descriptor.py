from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.tpeg_loc03_junction_point_descriptor_subtype_enum import (
    TpegLoc03JunctionPointDescriptorSubtypeEnum,
)
from ojp2.tpeg_point_descriptor import TpegPointDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    tpeg_junction_point_descriptor_type: Optional[
        TpegLoc03JunctionPointDescriptorSubtypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
