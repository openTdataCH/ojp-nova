from dataclasses import dataclass

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllowedResourceUsageExceededErrorStructure(ErrorCodeStructure):
    """Type for error.

    AllowedResourceUsageExceeded.
    """
