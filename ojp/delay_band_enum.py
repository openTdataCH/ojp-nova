from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class DelayBandEnum(Enum):
    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = "betweenTenMinutesAndThirtyMinutes"
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"
