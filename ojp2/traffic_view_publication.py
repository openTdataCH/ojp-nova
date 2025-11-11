from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.header_information import HeaderInformation
from ojp2.payload_publication import PayloadPublication
from ojp2.traffic_view import TrafficView

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficViewPublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    traffic_view: list[TrafficView] = field(
        default_factory=list,
        metadata={
            "name": "trafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
