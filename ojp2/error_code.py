from dataclasses import dataclass

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCode(ErrorCodeStructure):
    """
    Subsititutable type for a SIRI Error code.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
