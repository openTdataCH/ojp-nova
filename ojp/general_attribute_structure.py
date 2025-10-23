from dataclasses import dataclass, field
from typing import List, Optional
from ojp.access_facility_enumeration import AccessFacilityEnumeration
from ojp.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from ojp.assistance_facility_enumeration import AssistanceFacilityEnumeration
from ojp.fare_class_facility_enumeration import FareClassFacilityEnumeration
from ojp.hire_facility_enumeration import HireFacilityEnumeration
from ojp.international_text_structure import InternationalTextStructure
from ojp.luggage_facility_enumeration import LuggageFacilityEnumeration
from ojp.mobility_facility_enumeration import MobilityFacilityEnumeration
from ojp.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from ojp.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from ojp.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from ojp.refreshment_facility_enumeration import RefreshmentFacilityEnumeration
from ojp.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from ojp.ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeneralAttributeStructure:
    """
    Structured attribute classification with associated text.

    :ivar text: Text of the attribute to be shown to the user.
    :ivar code: Internal code of the attribute. Can be used for
        detection of double occurrences.
    :ivar fare_class_facility:
    :ivar ticketing_facility:
    :ivar nuisance_facility:
    :ivar mobility_facility:
    :ivar passenger_information_facility:
    :ivar passenger_comms_facility:
    :ivar refreshment_facility:
    :ivar access_facility: Classification of Access Facility.
    :ivar sanitary_facility:
    :ivar luggage_facility:
    :ivar accommodation_facility:
    :ivar assistance_facility:
    :ivar hire_facility:
    :ivar mandatory: Defines whether the attribute has to be shown to
        the user.
    :ivar importance: Importance of the attribute.
    :ivar info_url: URL to additional information on this general
        attribute. If available, the whole attribute text has to be used
        as the marked link.
    """
    text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    fare_class_facility: List[FareClassFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClassFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    ticketing_facility: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    nuisance_facility: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "NuisanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mobility_facility: List[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MobilityFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passenger_information_facility: List[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passenger_comms_facility: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    refreshment_facility: List[RefreshmentFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RefreshmentFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    access_facility: List[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    sanitary_facility: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    luggage_facility: List[LuggageFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LuggageFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accommodation_facility: List[AccommodationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    assistance_facility: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    hire_facility: List[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HireFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    importance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Importance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "max_inclusive": 100,
        }
    )
    info_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoURL",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
