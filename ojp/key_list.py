from dataclasses import dataclass
from ojp.key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class KeyList(KeyListStructure):
    """A list of alternative Key values for an element.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
