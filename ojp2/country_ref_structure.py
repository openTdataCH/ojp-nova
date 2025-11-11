from dataclasses import dataclass, field
from typing import Optional

from ojp2.iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class CountryRefStructure:
    """
    Type for reference to a Country identifier.
    """

    value: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
