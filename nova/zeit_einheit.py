from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString
from nova.zeit_einheit_code import ZeitEinheitCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class ZeitEinheit:
    """
    Eine Auflistung möglicher Zeiteinheiten.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    code: Optional[ZeitEinheitCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
