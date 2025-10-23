from dataclasses import dataclass, field
from typing import Optional
from nova.dauer import Dauer

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VorverkaufsFristTraegerMedium:
    vorverkaufs_frist: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "vorverkaufsFrist",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
