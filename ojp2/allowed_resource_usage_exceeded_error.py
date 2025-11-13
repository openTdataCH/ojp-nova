from dataclasses import dataclass

from ojp2.allowed_resource_usage_exceeded_error_structure import (
    AllowedResourceUsageExceededErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllowedResourceUsageExceededError(
    AllowedResourceUsageExceededErrorStructure
):
    """Error: Valid request was made but request would exceed the permitted resource usage of the client."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
