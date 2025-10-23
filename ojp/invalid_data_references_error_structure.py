from dataclasses import dataclass, field
from typing import List
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    """Type for InvalidDataReferencesError:.

    +SIRI v2.0.

    :ivar invalid_ref: Invalid reference values encoountered.
    """
    invalid_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InvalidRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
