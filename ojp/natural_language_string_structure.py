from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguageStringStructure:
    """
    Tyoe for a string in a specified language.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
