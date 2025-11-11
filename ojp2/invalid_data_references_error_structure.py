from dataclasses import dataclass, field

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    """Type for InvalidDataReferencesError:.

    (since SIRI 2.0).

    :ivar invalid_ref: Invalid reference values encoountered.
    """

    invalid_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InvalidRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
