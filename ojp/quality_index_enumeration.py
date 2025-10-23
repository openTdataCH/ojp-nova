from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class QualityIndexEnumeration(Enum):
    """Classification of the quality of the prediction of the CALL, according to a
    fixed list of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are stiull classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar CERTAIN: Data is certain (1/5).
    :cvar VERY_RELIABLE: Data has confidence level of very reliable
        (2/5).
    :cvar RELIABLE: Data has confidence lvel of reliabel (3/5).
    :cvar PROBABLY_RELIABLE: Data is thought to be reliable (4/5)
    :cvar UNCONFIRMED: Data is unconfirmed (5/5).
    """
    CERTAIN = "certain"
    VERY_RELIABLE = "veryReliable"
    RELIABLE = "reliable"
    PROBABLY_RELIABLE = "probablyReliable"
    UNCONFIRMED = "unconfirmed"
