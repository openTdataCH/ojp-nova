from dataclasses import dataclass, field
from typing import Optional

from ojp2.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class VehicleFilterStructure:
    """
    Filter for Vehicles.

    :ivar exclude: Whether to include or exclude given VehicleRefs and
        TRAIN NUMBERS in the list from the search. Default is exclude.
    :ivar vehicle_ref: Reference to VEHICLE
    :ivar train_number: TRAIN NUMBERs
    """

    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    vehicle_ref: list[VehicleRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    train_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
