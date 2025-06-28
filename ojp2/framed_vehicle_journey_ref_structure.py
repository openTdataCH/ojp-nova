from dataclasses import dataclass, field
from typing import Optional

from ojp2.data_frame_ref_structure import DataFrameRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FramedVehicleJourneyRefStructure:
    """
    Type for identifer of a VEHICLE JOURNEY within data Horizon of a service.

    :ivar data_frame_ref: identifier of data frame within particpant
        service. Used to ensure that the Reference to a DATED VEGICLE
        JOURNEY is unique with the data horizon of the service. Often
        the OperationalDayType is used for this purpose.
    :ivar dated_vehicle_journey_ref: A reference to the dated VEHICLE
        JOURNEY that the VEHICLE is making.
    """

    data_frame_ref: Optional[DataFrameRefStructure] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
