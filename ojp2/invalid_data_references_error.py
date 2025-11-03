from dataclasses import dataclass

from ojp2.invalid_data_references_error_structure import (
    InvalidDataReferencesErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    """Error: Request contains references to  identifiers that are not known.  (since SIRI 2.0)."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
