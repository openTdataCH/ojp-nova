from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class JourneyRelationTypeEnumeration(Enum):
    """
    Allowed types of relation between JOURNEYs.

    :cvar CONTINUATION_OF_JOURNEY: The journey is a continuation of the
        specified RelatedJourney at the stop point given in CallInfo.
        Passengers don't need to change vehicles. The new journey is not
        communicated as an interchange.
    :cvar CONTINUED_BY_JOURNEY: The journey is continued by the
        specified RelatedJourney at the stop point given in CallInfo.
        Passengers don't need to change vehicles. The new journey is not
        communicated as an interchange.
    :cvar SPLITS_INTO_JOURNEYS: The journey splits into multiple
        RelatedJourneys at the stop point given in CallInfo.
    :cvar CONTINUATION_OF_SPLIT_JOURNEY: The journey is a continuation
        of a single RelatedJourney splitting into multiple journeys at
        the stop point given in CallInfo.
    :cvar JOINING_OF_JOURNEYS: The journey is the continuation of
        multiple RelatedJourneys joining together at the stop point
        given in CallInfo.
    :cvar CONTINUED_BY_JOINED_JOURNEY: The journey is continued by a
        single RelatedJourney after joining other journeys at the stop
        point given in CallInfo.
    :cvar REPLACEMENT_OF_JOURNEY: The journey replaces one or more
        partially or fully cancelled RelatedJourneys during the
        JourneyPart defined or referenced in JourneyPartInfo.
    :cvar REPLACED_BY_JOURNEY: The partially or fully cancelled journey
        is replaced by one or more RelatedJourneys during the
        JourneyPart defined or referenced in JourneyPartInfo.
    :cvar SUPPORT_OF_JOURNEY: The journey partially or fully supports
        one or more RelatedJourneys during the JourneyPart defined or
        referenced in JourneyPartInfo.
    :cvar SUPPORTED_BY_JOURNEY: The journey is partially or fully
        supported by one or more RelatedJourneys during the JourneyPart
        defined or referenced in JourneyPartInfo.
    """

    CONTINUATION_OF_JOURNEY = "ContinuationOfJourney"
    CONTINUED_BY_JOURNEY = "ContinuedByJourney"
    SPLITS_INTO_JOURNEYS = "SplitsIntoJourneys"
    CONTINUATION_OF_SPLIT_JOURNEY = "ContinuationOfSplitJourney"
    JOINING_OF_JOURNEYS = "JoiningOfJourneys"
    CONTINUED_BY_JOINED_JOURNEY = "ContinuedByJoinedJourney"
    REPLACEMENT_OF_JOURNEY = "ReplacementOfJourney"
    REPLACED_BY_JOURNEY = "ReplacedByJourney"
    SUPPORT_OF_JOURNEY = "SupportOfJourney"
    SUPPORTED_BY_JOURNEY = "SupportedByJourney"
