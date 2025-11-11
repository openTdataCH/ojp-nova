from dataclasses import dataclass, field
from typing import Optional

from ojp2.air_submode import AirSubmode
from ojp2.alternative_modes_of_operation_enumeration import (
    AlternativeModesOfOperationEnumeration,
)
from ojp2.bus_submode import BusSubmode
from ojp2.coach_submode import CoachSubmode
from ojp2.conventional_modes_of_operation_enumeration import (
    ConventionalModesOfOperationEnumeration,
)
from ojp2.funicular_submode import FunicularSubmode
from ojp2.metro_submode import MetroSubmode
from ojp2.personal_modes_enumeration import PersonalModesEnumeration
from ojp2.personal_modes_of_operation_enumeration import (
    PersonalModesOfOperationEnumeration,
)
from ojp2.rail_submode import RailSubmode
from ojp2.telecabin_submode import TelecabinSubmode
from ojp2.tram_submode import TramSubmode
from ojp2.vehicle_modes_of_transport_enumeration import (
    VehicleModesOfTransportEnumeration,
)
from ojp2.water_submode import WaterSubmode

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ModeAndModeOfOperationFilterStructure:
    """
    List of MODE and MODE OF OPERATION filter offers to include or exclude.

    :ivar exclude: Whether MODE and MODE OF OPERATION combination in
        list are to include or exclude from search. Default is exclude.
    :ivar pt_mode: List of PT Transport modes to include/exclude. We use
        the SIRI 2.1 element which allows for many values in the
        enumeration. In OJP we don't use the following enumeration
        values: "pti1_xxx", "xxxServices" when a value without the
        "Service" exists for the same MODE, "allServicesExcept",
        "selfDrive", "taxi". Also, in cases where only a "xxxService"
        exists in the enumeration, it should be avoided. "other" or
        "unknown" should only be used if no other value applies.
    :ivar personal_mode: List of personal transport modes to
        include/exclude. Those are also used in many of the ALTERNATIVE
        MODES OF OPERATION.
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar funicular_submode:
    :ivar metro_submode:
    :ivar tram_submode:
    :ivar telecabin_submode:
    :ivar rail_submode:
    :ivar water_submode:
    :ivar personal_mode_of_operation: List of personal mobility offers
        to include/exclude.
    :ivar alternative_mode_of_operation: List of alternative mobility
        offers to include/exclude.
    :ivar conventional_mode_of_operation: List of conventional mobility
        offers to include/exclude.
    """

    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    pt_mode: list[VehicleModesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PtMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    personal_mode: list[PersonalModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PersonalMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    air_submode: list[AirSubmode] = field(
        default_factory=list,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bus_submode: list[BusSubmode] = field(
        default_factory=list,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    coach_submode: list[CoachSubmode] = field(
        default_factory=list,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    funicular_submode: list[FunicularSubmode] = field(
        default_factory=list,
        metadata={
            "name": "FunicularSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    metro_submode: list[MetroSubmode] = field(
        default_factory=list,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    tram_submode: list[TramSubmode] = field(
        default_factory=list,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    telecabin_submode: list[TelecabinSubmode] = field(
        default_factory=list,
        metadata={
            "name": "TelecabinSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    rail_submode: list[RailSubmode] = field(
        default_factory=list,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    water_submode: list[WaterSubmode] = field(
        default_factory=list,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    personal_mode_of_operation: list[PersonalModesOfOperationEnumeration] = (
        field(
            default_factory=list,
            metadata={
                "name": "PersonalModeOfOperation",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    alternative_mode_of_operation: list[
        AlternativeModesOfOperationEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeModeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    conventional_mode_of_operation: list[
        ConventionalModesOfOperationEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalModeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
