from dataclasses import dataclass, field
from typing import List
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParametersIgnoredErrorStructure(ErrorCodeStructure):
    """Type for Parameters Ignored Error:.

    +SIRI v2.0.

    :ivar parameter_name: Name of the unsupported parameter.
    """
    parameter_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
