from dataclasses import dataclass

from ojp2.message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MessageRefStructure(MessageQualifierStructure):
    """
    Type for reference to a message.
    """
