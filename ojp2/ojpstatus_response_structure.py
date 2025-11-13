from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.abstract_service_capabilities_response_structure import (
    AbstractServiceCapabilitiesResponseStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar service_started: Time when the service was started.
    :ivar service_ready: Time when the service started responding to
        queries.
    :ivar last_timetable_update: Time when the timetable was last
        updated.
    :ivar server_build_version: Information about the server build.
    :ivar extensions:
    """

    class Meta:
        name = "OJPStatusResponseStructure"

    data_frame_ref: Optional[DataFrameRefStructure] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    calc_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "CalcTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    service_started: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStarted",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    service_ready: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceReady",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    last_timetable_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastTimetableUpdate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    server_build_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServerBuildVersion",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
