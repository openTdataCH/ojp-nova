from dataclasses import dataclass, field
from typing import Optional

from ojp2.place_name_structure import PlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ViaNameStructure(PlaceNameStructure):
    """
    Type for VIA NAMes structure.

    :ivar via_priority: Relative priority to give to VIA name in
        displays. 1=high. Default is 2. (since SIRI 2.0)
    """

    via_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ViaPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
