from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ConfidentialityValueEnum(Enum):
    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = "restrictedToAuthoritiesAndTrafficOperators"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS = "restrictedToAuthoritiesTrafficOperatorsAndPublishers"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS = "restrictedToAuthoritiesTrafficOperatorsAndVms"
