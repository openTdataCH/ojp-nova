from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DelayBandEnumeration(Enum):
    """Type for allwoed values of Dela band.

    Based on Datex2
    """
    DELAY_TWO_MINUTES = "delayTwoMinutes"
    UP_TO_THREE_MINUTES = "upToThreeMinutes"
    UP_TO_FOUR_MINUTES = "upToFourMinutes"
    UP_TO_FIVE_MINUTES = "upToFiveMinutes"
    UP_TO_EIGHT_MINUTES = "upToEightMinutes"
    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = "betweenTenMinutesAndThirtyMinutes"
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"
