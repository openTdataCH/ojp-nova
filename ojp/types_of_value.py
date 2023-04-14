from dataclasses import dataclass
from ojp.types_of_value_structure import TypesOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TypesOfValue(TypesOfValueStructure):
    """VALUE SETs and TYPE OF VALUEs as part of the SIRI extension model.

    TYPES OF VALUE can be used to exchange metadata for validation or
    collection of data, such as the description and allowed values for
    codes. (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
