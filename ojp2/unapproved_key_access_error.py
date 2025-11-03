from dataclasses import dataclass

from ojp2.unapproved_key_access_structure import UnapprovedKeyAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnapprovedKeyAccessError(UnapprovedKeyAccessStructure):
    """Error:Recipient of a message to be distributed is not available.

    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
