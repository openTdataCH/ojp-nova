from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VerificationStatusEnumeration(Enum):
    """
    Values for Verification Status Corresponds to TPEG pti_table 32.
    """
    PTI32_0 = "pti32_0"
    UNKNOWN = "unknown"
    PTI32_1 = "pti32_1"
    UNVERIFIED = "unverified"
    PTI32_255 = "pti32_255"
    VERIFIED = "verified"
    VERIFIED_AS_DUPLICATE = "verifiedAsDuplicate"
