from dataclasses import dataclass, field
from typing import List, Optional
from ojp.access_modes_enumeration import AccessModesEnumeration
from ojp.air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration
from ojp.bus_submodes_of_transport_enumeration import BusSubmodesOfTransportEnumeration
from ojp.coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration
from ojp.empty_type import EmptyType
from ojp.metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration
from ojp.rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration
from ojp.tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration
from ojp.vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration
from ojp.water_submodes_of_transport_enumeration import WaterSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedModesStructure:
    """
    Type for TRANSPORT MODEs affecetd by a SITUATION.

    :ivar all_modes: All known modes for stop.
    :ivar mode: Mode affected by SITUATION.
    """
    all_modes: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mode: List["AffectedModesStructure.Mode"] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Mode:
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
