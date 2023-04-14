from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.non_road_event_information import NonRoadEventInformation
from ojp.transit_service_information_enum import TransitServiceInformationEnum
from ojp.transit_service_type_enum import TransitServiceTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TransitInformation(NonRoadEventInformation):
    journey_destination: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    journey_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    journey_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "journeyReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    transit_service_information: Optional[TransitServiceInformationEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    transit_service_type: Optional[TransitServiceTypeEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    scheduled_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "scheduledDepartureTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    transit_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "transitInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
