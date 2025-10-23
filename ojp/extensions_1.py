from dataclasses import dataclass
from ojp.extensions_structure import ExtensionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Extensions1(ExtensionsStructure):
    """Extensions to schema.

    (Wrapper tag used to avoid problems with handling of optional 'any'
    by some validators).
    """
    class Meta:
        name = "Extensions"
        namespace = "http://www.siri.org.uk/siri"
