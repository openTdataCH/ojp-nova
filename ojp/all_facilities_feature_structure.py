from dataclasses import dataclass, field
from typing import Optional
from ojp.access_facility_enumeration import AccessFacilityEnumeration
from ojp.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from ojp.assistance_facility_enumeration import AssistanceFacilityEnumeration
from ojp.fare_class_facility_enumeration import FareClassFacilityEnumeration
from ojp.hire_facility_enumeration import HireFacilityEnumeration
from ojp.luggage_facility_enumeration import LuggageFacilityEnumeration
from ojp.mobility_facility_enumeration import MobilityFacilityEnumeration
from ojp.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from ojp.parking_facility_enumeration import ParkingFacilityEnumeration
from ojp.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from ojp.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from ojp.refreshment_facility_enumeration import RefreshmentFacilityEnumeration
from ojp.reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration
from ojp.retail_facility_enumeration import RetailFacilityEnumeration
from ojp.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from ojp.ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllFacilitiesFeatureStructure:
    """
    Description of the features of any of the available facilities.
    """
    access_facility: Optional[AccessFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accommodation_facility: Optional[AccommodationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    assistance_facility: Optional[AssistanceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    fare_class_facility: Optional[FareClassFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClassFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    hire_facility: Optional[HireFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "HireFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    luggage_facility: Optional[LuggageFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "LuggageFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mobility_facility: Optional[MobilityFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    nuisance_facility: Optional[NuisanceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "NuisanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    parking_facility: Optional[ParkingFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passenger_comms_facility: Optional[PassengerCommsFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerCommsFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passenger_information_facility: Optional[PassengerInformationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    refreshment_facility: Optional[RefreshmentFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RefreshmentFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reserved_space_facility: Optional[ReservedSpaceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ReservedSpaceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    retail_facility: Optional[RetailFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RetailFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    sanitary_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "SanitaryFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    ticketing_facility: Optional[TicketingFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "TicketingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
