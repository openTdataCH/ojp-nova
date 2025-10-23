from dataclasses import dataclass, field
from typing import List, Optional
from ojp.international_text_structure import InternationalTextStructure
from ojp.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AddressStructure:
    """Descriptive data associated with a PLACE that can be used to describe the
    unique geographical context of a PLACE for the purposes of identifying it.

    May be refined as either a ROAD ADDRESS, a POSTAL ADDRESS or both

    :ivar address_code: ID of this address.
    :ivar private_code: Code of this address in
        private/foreign/proprietary coding schemes.
    :ivar address_name: Name or description of address for use in
        passenger information.
    :ivar name_suffix: Additional description of the address that may be
        appended to the name if enough space is available. F.e.
        "Crossing with Peterstraße".
    :ivar country_name: Country of the address.
    :ivar post_code: Postal code of the address.
    :ivar topographic_place_name: TopographicPlace name of the address.
        If set it should at least contain the city name.
    :ivar topographic_place_ref:
    :ivar street: Street name of the address.
    :ivar house_number: House number of the address. If none is given,
        either a crossing street can be given, or the whole street is
        meant.
    :ivar cross_road: Crossing. This can be used to be more specific
        without using house numbers.
    """
    address_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    private_code: List[PrivateCodeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    address_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "AddressName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    post_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    topographic_place_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    topographic_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    cross_road: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
