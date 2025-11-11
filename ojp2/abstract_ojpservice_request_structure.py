from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AbstractOjpserviceRequestStructure(
    AbstractFunctionalServiceRequestStructure
):
    """
    Basic request structure common for all OJP service requests.

    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar extension:
    """

    class Meta:
        name = "AbstractOJPServiceRequestStructure"

    data_frame_ref: Optional[DataFrameRefStructure] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
