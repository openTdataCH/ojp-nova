from dataclasses import dataclass
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllowedResourceUsageExceededErrorStructure(ErrorCodeStructure):
    """Type for error.

    AllowedResourceUsageExceeded.
    """
