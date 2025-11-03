from dataclasses import dataclass, field

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsErrorStructure(ErrorCodeStructure):
    """Type for Unknown Extensions Error:.

    (since SIRI 2.0).

    :ivar extension_name: Name of the unknown encountered extensions.
    """

    extension_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
