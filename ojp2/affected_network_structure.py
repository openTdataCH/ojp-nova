from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_modes_enumeration import AccessModesEnumeration
from ojp2.affected_operator_structure import AffectedOperatorStructure
from ojp2.affected_section_structure import AffectedSectionStructure
from ojp2.affected_stop_point_structure import (
    AffectedLineStructure,
    AffectedRouteStructure,
)
from ojp2.air_submode import AirSubmode
from ojp2.bus_submode import BusSubmode
from ojp2.coach_submode import CoachSubmode
from ojp2.empty_type import EmptyType
from ojp2.extensions_2 import Extensions2
from ojp2.metro_submode import MetroSubmode
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.network_ref_structure import NetworkRefStructure
from ojp2.rail_submode import RailSubmode
from ojp2.telecabin_submode import TelecabinSubmode
from ojp2.tram_submode import TramSubmode
from ojp2.vehicle_mode import VehicleMode
from ojp2.water_submode import WaterSubmode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedNetworkStructure:
    """Type for information about the parts of the network affected by an incident.

    If not explicitly overridden, modes and submodes will be defaulted
    to any values present in the general context.

    :ivar affected_operator: Operators of LINEs affected by incident.
        Overrides any value specified for (i) General Context.
    :ivar network_ref: Network of affected LINE. If absent, may be taken
        from context.
    :ivar network_name: Name of Network.  (Unbounded since SIRI 2.0)
    :ivar routes_affected: Textual description of overall routes
        affected. Should correspond to any structured description in the
        AffectedLines element.  (Unbounded since SIRI 2.0)
    :ivar vehicle_mode:
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar metro_submode:
    :ivar rail_submode:
    :ivar tram_submode:
    :ivar water_submode:
    :ivar telecabin_submode:
    :ivar access_mode:
    :ivar all_lines: All LINEs in the network are affected.
    :ivar selected_routes: Only some ROUTEs are affected,  LINE level
        information not available. See the RoutesAffected element for
        textual description.
    :ivar affected_section: Only some COMMON SECTIONs are affected, LINE
        level information not available.
    :ivar affected_line: Information about the indvidual LINEs in the
        network that are affected. If not explicitly overridden, modes
        and submodes will be defaulted to any values present (i) in the
        AffectedNetwork (ii) In the general context.
    :ivar extensions:
    """

    affected_operator: list[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_ref: Optional[NetworkRefStructure] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "NetworkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes_affected: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoutesAffected",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode: Optional[AirSubmode] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bus_submode: Optional[BusSubmode] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    coach_submode: Optional[CoachSubmode] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    metro_submode: Optional[MetroSubmode] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    rail_submode: Optional[RailSubmode] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    tram_submode: Optional[TramSubmode] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    water_submode: Optional[WaterSubmode] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    telecabin_submode: Optional[TelecabinSubmode] = field(
        default=None,
        metadata={
            "name": "TelecabinSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_lines: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllLines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    selected_routes: list[AffectedRouteStructure] = field(
        default_factory=list,
        metadata={
            "name": "SelectedRoutes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_section: list[AffectedSectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedSection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_line: list[AffectedLineStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedLine",
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
