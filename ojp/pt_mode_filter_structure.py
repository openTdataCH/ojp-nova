from dataclasses import dataclass, field
from typing import List, Optional
from ojp.air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration
from ojp.bus_submodes_of_transport_enumeration import BusSubmodesOfTransportEnumeration
from ojp.coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration
from ojp.funicular_submodes_of_transport_enumeration import FunicularSubmodesOfTransportEnumeration
from ojp.metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration
from ojp.rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration
from ojp.telecabin_submodes_of_transport_enumeration import TelecabinSubmodesOfTransportEnumeration
from ojp.tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration
from ojp.vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration
from ojp.water_submodes_of_transport_enumeration import WaterSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PtModeFilterStructure:
    """
    List of public transport modes ([from SIRI] mode of public transport service,
    corresponds to VEHICLE MODE) to include or exclude.

    :ivar exclude: Whether modes in list are to include or exclude from
        search. Default is exclude.
    :ivar pt_mode: List of PT Transport modes to include/exclude.
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar funicular_submode:
    :ivar metro_submode:
    :ivar tram_submode:
    :ivar telecabin_submode:
    :ivar rail_submode:
    :ivar water_submode:
    """
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    pt_mode: List[VehicleModesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PtMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    air_submode: List[AirSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    bus_submode: List[BusSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    coach_submode: List[CoachSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    funicular_submode: List[FunicularSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FunicularSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    metro_submode: List[MetroSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    tram_submode: List[TramSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    telecabin_submode: List[TelecabinSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TelecabinSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    rail_submode: List[RailSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    water_submode: List[WaterSubmodesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
