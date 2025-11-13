from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_facility_enumeration import AccessFacilityEnumeration
from ojp2.accommodation_facility import AccommodationFacility
from ojp2.call_at_stop_structure import CallAtStopStructure
from ojp2.dated_journey_structure import DatedJourneyStructure
from ojp2.fare_class_facility import FareClassFacility
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.leg_track_structure import LegTrackStructure
from ojp2.luggage_facility import LuggageFacility
from ojp2.mobility_facility import MobilityFacility
from ojp2.nuisance_facility import NuisanceFacility
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.operating_days_structure import OperatingDaysStructure
from ojp2.passenger_comms_facility import PassengerCommsFacility
from ojp2.passenger_information_facility import PassengerInformationFacility
from ojp2.refreshment_facility import RefreshmentFacility
from ojp2.sanitary_facility import SanitaryFacility
from ojp2.ticketing_facility import TicketingFacility
from ojp2.vehicle_position_structure import VehiclePositionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoResultStructure:
    """
    TripInfo result structure containing the status of a trip.

    :ivar error_condition: Problems related to this TripInfo result.
    :ivar previous_call: The stops this service already has called at.
        Including the current stop if service is currently at stop.
    :ivar current_position: Current position of this service.
    :ivar onward_call: The stops this service still has to call at.
    :ivar service: Description of the service.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g., "Monday to Friday" or "not on holidays".
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

    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    previous_call: list[CallAtStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    current_position: Optional[VehiclePositionStructure] = field(
        default=None,
        metadata={
            "name": "CurrentPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    onward_call: list[CallAtStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    service: Optional[DatedJourneyStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_class_facility: list[FareClassFacility] = field(
        default_factory=list,
        metadata={
            "name": "FareClassFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ticketing_facility: list[TicketingFacility] = field(
        default_factory=list,
        metadata={
            "name": "TicketingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    nuisance_facility: list[NuisanceFacility] = field(
        default_factory=list,
        metadata={
            "name": "NuisanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mobility_facility: list[MobilityFacility] = field(
        default_factory=list,
        metadata={
            "name": "MobilityFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_information_facility: list[PassengerInformationFacility] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_comms_facility: list[PassengerCommsFacility] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    refreshment_facility: list[RefreshmentFacility] = field(
        default_factory=list,
        metadata={
            "name": "RefreshmentFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_facility: list[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sanitary_facility: list[SanitaryFacility] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    luggage_facility: list[LuggageFacility] = field(
        default_factory=list,
        metadata={
            "name": "LuggageFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accommodation_facility: list[AccommodationFacility] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "JourneyTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
