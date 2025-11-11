from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VehicleDetectionTime:
    arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "arrivalTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exit_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "exitTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    passage_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "passageTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    presence_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "presenceTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_detection_time_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleDetectionTimeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
