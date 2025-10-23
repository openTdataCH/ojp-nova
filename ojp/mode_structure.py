from dataclasses import dataclass, field
from typing import Optional
from ojp.air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration
from ojp.bus_submodes_of_transport_enumeration import BusSubmodesOfTransportEnumeration
from ojp.coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration
from ojp.funicular_submodes_of_transport_enumeration import FunicularSubmodesOfTransportEnumeration
from ojp.international_text_structure import InternationalTextStructure
from ojp.metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration
from ojp.rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration
from ojp.telecabin_submodes_of_transport_enumeration import TelecabinSubmodesOfTransportEnumeration
from ojp.tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration
from ojp.vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration
from ojp.water_submodes_of_transport_enumeration import WaterSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ModeStructure:
    """
    [a specialisation of MODE in TMv6] an extended range of VEHICLE MODEs,
    aggregating them with some SUBMODEs.

    :ivar pt_mode: Categorisation of mode
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar funicular_submode:
    :ivar metro_submode:
    :ivar tram_submode:
    :ivar telecabin_submode:
    :ivar rail_submode:
    :ivar water_submode:
    :ivar name: Name of the mode.
    :ivar short_name: Short name or acronym of the mode.
    :ivar description: Additional text that further describes the mode.
    """
    pt_mode: Optional[VehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "PtMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
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
    funicular_submode: Optional[FunicularSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "FunicularSubmode",
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
    tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    telecabin_submode: Optional[TelecabinSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TelecabinSubmode",
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
    water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    short_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
