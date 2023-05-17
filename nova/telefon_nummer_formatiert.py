from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class TelefonNummerFormatiert:
    """
    :ivar wert:
    :ivar formatiert_e123: @Deprecated Will be removed with NOVA 15.
        Phone number can be formatted by client with for example
        libphonenumber (https://github.com/google/libphonenumber)
    :ivar version_telefon_nummer:
    """
    wert: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 16,
        }
    )
    formatiert_e123: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatiertE123",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 16,
        }
    )
    version_telefon_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionTelefonNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
