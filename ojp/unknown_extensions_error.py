from dataclasses import dataclass
from ojp.unknown_extensions_error_structure import UnknownExtensionsErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsError(UnknownExtensionsErrorStructure):
    """Error: Request contained extensions that were not supported by the producer. A response has been provided but some or all extensions have been ignored..  +SIRI v2.0."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
