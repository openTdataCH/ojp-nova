from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_modes_enumeration import AccessModesEnumeration
from ojp2.air_submode import AirSubmode
from ojp2.bus_submode import BusSubmode
from ojp2.coach_submode import CoachSubmode
from ojp2.empty_type import EmptyType
from ojp2.metro_submode import MetroSubmode
from ojp2.rail_submode import RailSubmode
from ojp2.telecabin_submode import TelecabinSubmode
from ojp2.tram_submode import TramSubmode
from ojp2.vehicle_mode import VehicleMode
from ojp2.water_submode import WaterSubmode

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
        },
    )
    mode: list["AffectedModesStructure.Mode"] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Mode:
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
