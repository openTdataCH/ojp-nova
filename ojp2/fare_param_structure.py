from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_modes_list_of_enumerations import (
    AccessModesListOfEnumerations,
)
from ojp2.fare_authority_ref_structure import FareAuthorityRefStructure
from ojp2.fare_class_enumeration import FareClassEnumeration
from ojp2.fare_passenger_structure import FarePassengerStructure
from ojp2.passenger_category_enumeration import PassengerCategoryEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareParamStructure:
    """
    [related to the FARE parameter model in TM and NeTEx] parameters which are used
    to determine the price to be paid for a FARE PRODUCT by a specific passenger.

    :ivar fare_authority_filter: Fare authority for which to retrieve
        Fare information.
    :ivar passenger_category: sequence of all passenger categories, for
        which this FareProduct is valid
    :ivar fare_class: Fare class for which to retrieve FareProducts.
        Refers to TYPE OF FARE CLASS (e.g., first class). Transmodel:
        CLASS OF USE.
    :ivar traveller: Number of travellers that will make the journey and
        for which Fare information needs to be gathered.
    :ivar access_mode_list: ACCESS MODEs to consider (usually only one).
        This is only used in very special cases. E.g. for
        carTransportRail. It indicates if one uses a car, truck,
        motorcycle or bike. The Access mode may result in no
        transportation being possible.
    :ivar extension:
    """

    fare_authority_filter: list[FareAuthorityRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareAuthorityFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    passenger_category: list[PassengerCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    traveller: list[FarePassengerStructure] = field(
        default_factory=list,
        metadata={
            "name": "Traveller",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    access_mode_list: Optional[AccessModesListOfEnumerations] = field(
        default=None,
        metadata={
            "name": "AccessModeList",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
