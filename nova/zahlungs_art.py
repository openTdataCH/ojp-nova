from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ZahlungsArt:
    """
    :ivar bezeichnung:
    :ivar zahlungs_art_code: UNBEKANNT; BAR; BON; MAE; FAK; DOS; DIN;
        AMX; JCB; VEG; VIS; PCD; YWD; MC; EC; MIG; ONE; REK; UAP
    :ivar kurz_text:
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    zahlungs_art_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zahlungsArtCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    kurz_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "kurzText",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )
