from dataclasses import dataclass, field
from typing import List
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsErrorStructure(ErrorCodeStructure):
    """Type for Unknown Extensions Error:.

    +SIRI v2.0.

    :ivar extension_name: Name of the unknown encountered extensions.
    """
    extension_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
