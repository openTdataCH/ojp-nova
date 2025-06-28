from dataclasses import dataclass

from ojp2.type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TypeOfValue(TypeOfValueStructure):
    """A code value from an extensible set which may be added to by user
    applications, and is used to classify other SIRI entities.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
