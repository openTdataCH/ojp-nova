from dataclasses import dataclass, field
from typing import List, Optional
from ojp.elaborated_data import ElaboratedData
from ojp.extension_type import ExtensionType
from ojp.operator_action import OperatorAction
from ojp.traffic_element import TrafficElement
from ojp.url_link import UrlLink

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficViewRecord:
    record_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "recordSequenceNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    traffic_element: Optional[TrafficElement] = field(
        default=None,
        metadata={
            "name": "trafficElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    operator_action: Optional[OperatorAction] = field(
        default=None,
        metadata={
            "name": "operatorAction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    elaborated_data: Optional[ElaboratedData] = field(
        default=None,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    traffic_view_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewRecordExtension",
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
