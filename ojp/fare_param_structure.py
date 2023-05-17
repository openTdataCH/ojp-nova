from dataclasses import dataclass, field
from typing import List, Optional
from ojp.fare_passenger_structure import FarePassengerStructure
from ojp.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp.type_of_fare_class_enumeration import TypeOfFareClassEnumeration

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
    :ivar travel_class: Travel class for which to retrieve FareProducts.
        Refers to TYPE OF FARE CLASS
    :ivar traveller: Number of travellers that will make the journey and
        for which Fare information needs to be gathered.
    """
    fare_authority_filter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FareAuthorityFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    passenger_category: List[PassengerCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    travel_class: Optional[TypeOfFareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "TravelClass",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    traveller: List[FarePassengerStructure] = field(
        default_factory=list,
        metadata={
            "name": "Traveller",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
