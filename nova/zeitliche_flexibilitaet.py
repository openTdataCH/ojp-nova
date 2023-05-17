from dataclasses import dataclass, field
from typing import Optional
from nova.uhrzeit_einschraenkungen_typ import UhrzeitEinschraenkungenTyp
from nova.zonen_befahrungs_typ import ZonenBefahrungsTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ZeitlicheFlexibilitaet:
    uhrzeit_einschraenkungen: Optional[UhrzeitEinschraenkungenTyp] = field(
        default=None,
        metadata={
            "name": "uhrzeitEinschraenkungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    zonen_befahrungs_typ: Optional[ZonenBefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "zonenBefahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
