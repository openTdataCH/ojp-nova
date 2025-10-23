from dataclasses import dataclass, field
from typing import Optional
from nova.fahr_art_typ_code import FahrArtTypCode
from nova.localized_string import LocalizedString
from nova.segment_typ import SegmentTyp
from nova.verkehrs_mittel_typ_code import VerkehrsMittelTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ReiseRouteSegment:
    """Die Generalisierung ReiserouteSegment steht für verschiedene Typen von
    Segmenten aus denen (durch Aneinanderreihung) eine für den Kunden relevante
    Information (bzgl.

    des Reisewegs und der ReisendenInfo) aufgebaut werden kann.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    segment_typ: Optional[SegmentTyp] = field(
        default=None,
        metadata={
            "name": "segmentTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    uic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "uicCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_inclusive": 0,
        }
    )
    fahr_art_typ: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "name": "fahrArtTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    verkehrs_mittel_typ: Optional[VerkehrsMittelTypCode] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
