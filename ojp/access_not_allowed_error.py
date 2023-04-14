from dataclasses import dataclass
from ojp.access_not_allowed_error_structure import AccessNotAllowedErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AccessNotAllowedError(AccessNotAllowedErrorStructure):
    """Error: Requestor is not authorised to the service or data requested."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
