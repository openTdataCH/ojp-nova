from dataclasses import dataclass, field
from typing import Optional

from ojp2.air_submode import AirSubmode
from ojp2.bus_submode import BusSubmode
from ojp2.coach_submode import CoachSubmode
from ojp2.funicular_submode import FunicularSubmode
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.metro_submode import MetroSubmode
from ojp2.rail_submode import RailSubmode
from ojp2.telecabin_submode import TelecabinSubmode
from ojp2.tram_submode import TramSubmode
from ojp2.vehicle_modes_of_transport_enumeration import (
    VehicleModesOfTransportEnumeration,
)
from ojp2.water_submode import WaterSubmode

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ModeStructure:
    """
    [a specialisation of MODE in TMv6] an extended range of VEHICLE MODEs,
    aggregating them with some SUBMODEs.

    :ivar pt_mode: Categorisation of a (conventional) PUBLIC TRANSPORT
        MODE. We use the SIRI 2.1 element which allows for many values
        in the enumeration. In OJP we don't use the following
        enumeration values: "pti1_xxx", "xxxServices" when a value
        without the "Service" exists for the same MODE,
        "allServicesExcept", "selfDrive", "taxi". Also, in cases where
        only a "xxxService" exists in the enumeration, it should be
        avoided. "other" or "unknown" should only be used if no other
        value applies.
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
    funicular_submode: Optional[FunicularSubmode] = field(
        default=None,
        metadata={
            "name": "FunicularSubmode",
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
    tram_submode: Optional[TramSubmode] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
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
    rail_submode: Optional[RailSubmode] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
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
    name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    short_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
