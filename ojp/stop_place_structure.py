from dataclasses import dataclass, field
from typing import List, Optional
from ojp.international_text_structure import InternationalTextStructure
from ojp.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopPlaceStructure:
    """
    [an extended view of STOP PLACE in TMv6] a PLACE extended by ACCESSIBILITY
    LIMITATION properties and some attributes of the associated equipment,
    comprising one or more locations where vehicles may stop and where
    passengers may board or leave vehicles or prepare their trip, and which
    will usually have one or more wellknown names.

    :ivar stop_place_ref:
    :ivar stop_place_name: Name of this stop place for use in passenger
        information.
    :ivar name_suffix: Additional description of the stop place that may
        be appended to the name if enough space is available. F.e.
        "Exhibition Center".
    :ivar private_code: Code of this stop place in
        private/foreign/proprietary coding schemes.
    :ivar topographic_place_ref:
    :ivar wheelchair_accessible: Whether this stop is accessible for
        wheelchair users.
    :ivar lighting: Whether this stop is lit.
    :ivar covered: Whether this stop offers protection from weather
        conditions like rain, snow, storm etc.
    """
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    stop_place_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    private_code: List[PrivateCodeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    topographic_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    lighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    covered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
