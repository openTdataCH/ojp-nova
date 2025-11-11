from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_facility import AccessFacility
from ojp2.accommodation_facility import AccommodationFacility
from ojp2.assistance_facility import AssistanceFacility
from ojp2.fare_class_facility import FareClassFacility
from ojp2.hire_facility import HireFacility
from ojp2.luggage_facility import LuggageFacility
from ojp2.mobility_facility import MobilityFacility
from ojp2.nuisance_facility import NuisanceFacility
from ojp2.parking_facility import ParkingFacility
from ojp2.passenger_comms_facility import PassengerCommsFacility
from ojp2.passenger_information_facility import PassengerInformationFacility
from ojp2.refreshment_facility import RefreshmentFacility
from ojp2.reserved_space_facility import ReservedSpaceFacility
from ojp2.retail_facility import RetailFacility
from ojp2.sanitary_facility import SanitaryFacility
from ojp2.ticketing_facility import TicketingFacility

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllFacilitiesFeatureStructure:
    """
    Description of the features of any of the available facilities.
    """

    access_facility: Optional[AccessFacility] = field(
        default=None,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accommodation_facility: Optional[AccommodationFacility] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    assistance_facility: Optional[AssistanceFacility] = field(
        default=None,
        metadata={
            "name": "AssistanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fare_class_facility: Optional[FareClassFacility] = field(
        default=None,
        metadata={
            "name": "FareClassFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    hire_facility: Optional[HireFacility] = field(
        default=None,
        metadata={
            "name": "HireFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    luggage_facility: Optional[LuggageFacility] = field(
        default=None,
        metadata={
            "name": "LuggageFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mobility_facility: Optional[MobilityFacility] = field(
        default=None,
        metadata={
            "name": "MobilityFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    nuisance_facility: Optional[NuisanceFacility] = field(
        default=None,
        metadata={
            "name": "NuisanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    parking_facility: Optional[ParkingFacility] = field(
        default=None,
        metadata={
            "name": "ParkingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_comms_facility: Optional[PassengerCommsFacility] = field(
        default=None,
        metadata={
            "name": "PassengerCommsFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_information_facility: Optional[PassengerInformationFacility] = (
        field(
            default=None,
            metadata={
                "name": "PassengerInformationFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    refreshment_facility: Optional[RefreshmentFacility] = field(
        default=None,
        metadata={
            "name": "RefreshmentFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reserved_space_facility: Optional[ReservedSpaceFacility] = field(
        default=None,
        metadata={
            "name": "ReservedSpaceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    retail_facility: Optional[RetailFacility] = field(
        default=None,
        metadata={
            "name": "RetailFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sanitary_facility: Optional[SanitaryFacility] = field(
        default=None,
        metadata={
            "name": "SanitaryFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ticketing_facility: Optional[TicketingFacility] = field(
        default=None,
        metadata={
            "name": "TicketingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
