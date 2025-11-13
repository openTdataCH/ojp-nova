from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.place_context_structure import PlaceContextStructure
from ojp2.stop_event_param_structure import StopEventParamStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar location: LOCATION / PLACE for which to obtain stop event
        information. If a coordinate or an address is used, then the
        result may depend on other parameters: All stops in reasonable
        walking distance and stops that are within range of limitations
        of the IndividualTransportOptions should be shown. If the next
        stop is too far away, then no result is shown. "Reasonable" is
        usually defined as part of the server configuration.
    :ivar params: Request parameter
    :ivar extensions:
    """

    class Meta:
        name = "OJPStopEventRequestStructure"

    location: Optional[PlaceContextStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    params: Optional[StopEventParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
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
