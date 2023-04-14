from dataclasses import dataclass, field
from typing import List, Optional
from ojp.access_modes_enumeration import AccessModesEnumeration
from ojp.affected_line_structure import AffectedLineStructure
from ojp.affected_operator_structure import AffectedOperatorStructure
from ojp.air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration
from ojp.bus_submodes_of_transport_enumeration import BusSubmodesOfTransportEnumeration
from ojp.coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration
from ojp.empty_type import EmptyType
from ojp.extensions_1 import Extensions1
from ojp.metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration
from ojp.tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration
from ojp.vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration
from ojp.water_submodes_of_transport_enumeration import WaterSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedNetworkStructure:
    """Type for information about the parts of the network affected by an
    incident.

    If not explclitly overrided Modes and submodes will be defaulted to
    any values present in the general Context.

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
    :ivar access_mode:
    :ivar all_lines: All LINEs in the network are affected.
    :ivar selected_routes: Only some ROUTEs are affected,  LINE level
        information not available. See the AffectedRoutes element for
        textual description.
    :ivar affected_line: Information about the indvidual LINEs in the
        network that are affected. If not explclitly overrided Modes and
        submodes will be defaulted to any values present (i) in the
        AffectedNetwork (ii) In the general Context.
    :ivar extensions:
    """
    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    network_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    network_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "NetworkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    routes_affected: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoutesAffected",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    vehicle_mode: Optional[VehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    air_submode: Optional[AirSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    bus_submode: Optional[BusSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    coach_submode: Optional[CoachSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    metro_submode: Optional[MetroSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    rail_submode: Optional[RailSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    all_lines: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllLines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    selected_routes: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "SelectedRoutes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_line: List[AffectedLineStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedLine",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
