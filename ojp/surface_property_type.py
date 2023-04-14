from dataclasses import dataclass, field
from typing import Optional, Union
from ojp.nil_reason_enumeration_value import NilReasonEnumerationValue
from ojp.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
