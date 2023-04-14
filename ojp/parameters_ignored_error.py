from dataclasses import dataclass
from ojp.parameters_ignored_error_structure import ParametersIgnoredErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParametersIgnoredError(ParametersIgnoredErrorStructure):
    """Error: Request contained parameters that were not supported by the producer. A response has been provided but some parameters have been ignored. +SIRI v2.0."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
