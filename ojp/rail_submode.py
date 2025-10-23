from dataclasses import dataclass, field
from ojp.rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RailSubmode:
    """
    TPEG pti02 Rail submodes loc13.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RailSubmodesOfTransportEnumeration = field(
        default=RailSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
