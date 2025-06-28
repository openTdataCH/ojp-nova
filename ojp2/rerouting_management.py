from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.itinerary import Itinerary
from ojp2.multilingual_string import MultilingualString
from ojp2.network_management import NetworkManagement
from ojp2.rerouting_management_type_enum import ReroutingManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ReroutingManagement(NetworkManagement):
    rerouting_management_type: list[ReroutingManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    rerouting_itinerary_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reroutingItineraryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    signed_rerouting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "signedRerouting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    entry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    exit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    road_or_junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadOrJunctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    alternative_route: list[Itinerary] = field(
        default_factory=list,
        metadata={
            "name": "alternativeRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    rerouting_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "reroutingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
