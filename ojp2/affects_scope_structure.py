from dataclasses import dataclass, field
from typing import Optional

from ojp2.affected_network_structure import AffectedNetworkStructure
from ojp2.affected_operator_structure import AffectedOperatorStructure
from ojp2.affected_place_structure import AffectedPlaceStructure
from ojp2.affected_roads_structure import AffectedRoadsStructure
from ojp2.affected_stop_point_structure import (
    AffectedStopPlaceStructure,
    AffectedStopPointStructure,
)
from ojp2.affected_vehicle_journey_structure import (
    AffectedVehicleJourneyStructure,
)
from ojp2.affected_vehicle_structure import AffectedVehicleStructure
from ojp2.area_of_interest_enum import AreaOfInterestEnum
from ojp2.empty_type import EmptyType
from ojp2.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectsScopeStructure:
    """
    Type for Location model for scope of SITUATION or effect.

    :ivar area_of_interest: Affected overall Geographic scope.
    :ivar operators: Affected OPERATORs, If absent, taken from context.
        If present, any OPERATORs stated completely replace those from
        context.
    :ivar networks: Networks affected by SITUATION.
    :ivar stop_points: STOP POINTs affected by SITUATION.
    :ivar stop_places: Places other than STOP POINTs affected by
        SITUATION.
    :ivar places: Places other than STOP POINTs affected by SITUATION.
    :ivar vehicle_journeys: Specific journeys affected by SITUATION.
    :ivar vehicles: Specific vehicles affected by SITUATION. ((since
        SIRI 2.0))
    :ivar roads: Roads affected by.
    :ivar extensions:
    """

    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "AreaOfInterest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operators: Optional["AffectsScopeStructure.Operators"] = field(
        default=None,
        metadata={
            "name": "Operators",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    networks: Optional["AffectsScopeStructure.Networks"] = field(
        default=None,
        metadata={
            "name": "Networks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectsScopeStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_places: Optional["AffectsScopeStructure.StopPlaces"] = field(
        default=None,
        metadata={
            "name": "StopPlaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    places: Optional["AffectsScopeStructure.Places"] = field(
        default=None,
        metadata={
            "name": "Places",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journeys: Optional["AffectsScopeStructure.VehicleJourneys"] = (
        field(
            default=None,
            metadata={
                "name": "VehicleJourneys",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    vehicles: Optional["AffectsScopeStructure.Vehicles"] = field(
        default=None,
        metadata={
            "name": "Vehicles",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    roads: Optional[AffectedRoadsStructure] = field(
        default=None,
        metadata={
            "name": "Roads",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Operators:
        """
        :ivar all_operators: All OPERATORs.
        :ivar affected_operator: Operators of services affected by
            SITUATION.
        """

        all_operators: Optional[EmptyType] = field(
            default=None,
            metadata={
                "name": "AllOperators",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        affected_operator: list[AffectedOperatorStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedOperator",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class Networks:
        """
        :ivar affected_network: Networks and Route(s) affected by
            SITUATION.
        """

        affected_network: list[AffectedNetworkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedNetwork",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPoints:
        """
        :ivar affected_stop_point: STOP POINT affected by SITUATION.
        """

        affected_stop_point: list[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPlaces:
        """
        :ivar affected_stop_place: STOP PLACE affected by SITUATION.
        """

        affected_stop_place: list[AffectedStopPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Places:
        """
        :ivar affected_place: Place affected by SITUATION.
        """

        affected_place: list[AffectedPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class VehicleJourneys:
        """
        :ivar affected_vehicle_journey: Journeys affected by the
            SITUATION.
        """

        affected_vehicle_journey: list[AffectedVehicleJourneyStructure] = (
            field(
                default_factory=list,
                metadata={
                    "name": "AffectedVehicleJourney",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_occurs": 1,
                },
            )
        )

    @dataclass
    class Vehicles:
        """
        :ivar affected_vehicle: Vehicles affected by the SITUATION.
            ((since SIRI 2.0))
        """

        affected_vehicle: list[AffectedVehicleStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedVehicle",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
