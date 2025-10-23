from dataclasses import dataclass, field
from typing import Optional
from ojp.access_not_allowed_error import AccessNotAllowedError
from ojp.allowed_resource_usage_exceeded_error import AllowedResourceUsageExceededError
from ojp.beyond_data_horizon import BeyondDataHorizon
from ojp.capability_not_supported_error import CapabilityNotSupportedError
from ojp.invalid_data_references_error import InvalidDataReferencesError
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.no_info_for_topic_error import NoInfoForTopicError
from ojp.other_error import OtherError
from ojp.parameters_ignored_error import ParametersIgnoredError
from ojp.service_not_available_error import ServiceNotAvailableError
from ojp.unknown_extensions_error import UnknownExtensionsError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorConditionStructure:
    """
    Type for RequestErrorCondition.

    :ivar service_not_available_error:
    :ivar capability_not_supported_error:
    :ivar access_not_allowed_error:
    :ivar invalid_data_references_error:
    :ivar beyond_data_horizon: Error: Data period or subscription period
        is outside of period covered by service.   +SIRI v2.0.
    :ivar no_info_for_topic_error:
    :ivar parameters_ignored_error:
    :ivar unknown_extensions_error: Error: Request contained extensions
        that were not supported by the producer. A response has been
        provided but some or all extensions have been ignored.  +SIRI
        v2.0.
    :ivar allowed_resource_usage_exceeded_error:
    :ivar other_error:
    :ivar description: Text description of error.
    """
    service_not_available_error: Optional[ServiceNotAvailableError] = field(
        default=None,
        metadata={
            "name": "ServiceNotAvailableError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
        default=None,
        metadata={
            "name": "CapabilityNotSupportedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    access_not_allowed_error: Optional[AccessNotAllowedError] = field(
        default=None,
        metadata={
            "name": "AccessNotAllowedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    invalid_data_references_error: Optional[InvalidDataReferencesError] = field(
        default=None,
        metadata={
            "name": "InvalidDataReferencesError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    beyond_data_horizon: Optional[BeyondDataHorizon] = field(
        default=None,
        metadata={
            "name": "BeyondDataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    no_info_for_topic_error: Optional[NoInfoForTopicError] = field(
        default=None,
        metadata={
            "name": "NoInfoForTopicError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    parameters_ignored_error: Optional[ParametersIgnoredError] = field(
        default=None,
        metadata={
            "name": "ParametersIgnoredError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    unknown_extensions_error: Optional[UnknownExtensionsError] = field(
        default=None,
        metadata={
            "name": "UnknownExtensionsError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    allowed_resource_usage_exceeded_error: Optional[AllowedResourceUsageExceededError] = field(
        default=None,
        metadata={
            "name": "AllowedResourceUsageExceededError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    other_error: Optional[OtherError] = field(
        default=None,
        metadata={
            "name": "OtherError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
