from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VerificationStatusEnumeration(Enum):
    """Values for TPEG Pti032 - VerificationStatus

    :cvar UNKNOWN: TPEG Pti32_0, unknown
    :cvar UNVERIFIED: TPEG Pti32_1, unverified
    :cvar VERIFIED: TPEG Pti32_?, verified
    :cvar VERIFIED_AS_DUPLICATE: TPEG Pti32_?, verifiedAsDuplicate
    :cvar UNDEFINED: TPEG Pti32_255 ?
    """

    UNKNOWN = "unknown"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    VERIFIED_AS_DUPLICATE = "verifiedAsDuplicate"
    UNDEFINED = "undefined"
