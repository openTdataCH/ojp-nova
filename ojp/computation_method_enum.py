from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ComputationMethodEnum(Enum):
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "arithmeticAverageOfSamplesInATimePeriod"
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "harmonicAverageOfSamplesInATimePeriod"
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"
