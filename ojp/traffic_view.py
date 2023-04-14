from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extension_type import ExtensionType
from ojp.linear_traffic_view import LinearTrafficView

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficView:
    traffic_view_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "trafficViewTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    linear_traffic_view: List[LinearTrafficView] = field(
        default_factory=list,
        metadata={
            "name": "linearTrafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
