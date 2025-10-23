from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class NonRoadEventInformation(SituationRecord):
    non_road_event_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonRoadEventInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
