from dataclasses import dataclass
from ojp.value_set_structure import ValueSetStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ValueSet(ValueSetStructure):
    """An extensible set of code values which may be added to by user
    applications and is used to validate the properties of entities.

    Contains TYPE OF VALUEs that are an instance of the same class.
    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
