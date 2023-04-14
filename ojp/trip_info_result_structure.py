from dataclasses import dataclass, field
from typing import List, Optional
from ojp.access_facility_enumeration import AccessFacilityEnumeration
from ojp.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from ojp.call_at_stop_structure import CallAtStopStructure
from ojp.dated_journey_structure import DatedJourneyStructure
from ojp.fare_class_facility_enumeration import FareClassFacilityEnumeration
from ojp.international_text_structure import InternationalTextStructure
from ojp.leg_track_structure import LegTrackStructure
from ojp.luggage_facility_enumeration import LuggageFacilityEnumeration
from ojp.mobility_facility_enumeration import MobilityFacilityEnumeration
from ojp.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from ojp.operating_days_structure import OperatingDaysStructure
from ojp.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from ojp.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from ojp.refreshment_facility_enumeration import RefreshmentFacilityEnumeration
from ojp.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from ojp.ticketing_facility_enumeration import TicketingFacilityEnumeration
from ojp.vehicle_position_structure import VehiclePositionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoResultStructure:
    """
    TripInfo result structure containing the current status of a trip.

    :ivar previous_call: The stops this service already has called at.
        Including the current stop if service is currently at stop.
    :ivar current_position: Current position of this service.
    :ivar onward_call: The stops this service still has to call at.
    :ivar service: Description of the service.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g. "monday to friday" or "not on holidays".
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
    :ivar journey_track: Geographic embedding of this journey. The
        entire journey is regarded as one leg.
    :ivar extension:
    """
    previous_call: List[CallAtStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    current_position: Optional[VehiclePositionStructure] = field(
        default=None,
        metadata={
            "name": "CurrentPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    onward_call: List[CallAtStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    service: Optional[DatedJourneyStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    journey_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "JourneyTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
