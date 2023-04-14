from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class LocalizedString:
    """Der Basisdatentyp LocalizedString wird für alle Texte / Zeichenketten
    verwendet, die auf der öV-Plattform internationalisiert werden.

    Das Objekt LocalizedString bietet in Abhängigkeit von der Locale die
    entsprechenden Übersetzungen der Texte / Zeichenketten.
    """
    default_wert: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultWert",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    de: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    en: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    fr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    it: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
