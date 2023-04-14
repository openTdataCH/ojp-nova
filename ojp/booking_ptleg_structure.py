from dataclasses import dataclass, field
from typing import List, Optional
from ojp.general_attribute_structure import GeneralAttributeStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.mode_structure import ModeStructure
from ojp.operator_refs_rel_structure import OperatorRefsRelStructure
from ojp.product_category_structure_2 import ProductCategoryStructure2
from ojp.provisioned_call_at_place_structure import ProvisionedCallAtPlaceStructure
from ojp.service_via_point_structure import ServiceViaPointStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingPtlegStructure:
    """
    Journey leg by public transport.

    :ivar pick_up_location: Location where passenger intends to enter
        the service.
    :ivar set_down_location: Location where passenger intends to leave
        the service.
    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    :ivar mode: [a specialisation of MODE in TMv6] an extended range of
        VEHICLE MODEs, aggregating them with some SUBMODEs
    :ivar product_category: A product category for the service. This is
        a classification defined in NeTEx/SIRI used to identify groups
        of journeys with some special properties for marketing and fare
        products, e.g. "TE2" for SNCF or a special panorama train "PE"
        in Switzerland.
    :ivar published_service_name: Line name or service description as
        known to the public, f.e. "512", "S8" or "Circle Line" or "ICE
        488".
    :ivar train_number: Contains the TrainNumber from NeTEx (TRAIN
        NUMBER from Transmodel). If several TrainNumber types exist, use
        the commercial one. In some cases also non-train modes will use
        TrainNumber.
    :ivar vehicle_ref: Contains the Vehicle reference of the vehicle. In
        Transmodel this may be the VEHICLE Id.
    :ivar operator_refs: References to the OPERATORS. Multiple OPERATORS
        in case a ContinuousLeg can be operated by more than one
        operator, especially in the ALTERNATIVE MODE OF OPERATION where
        there can be dozens of taxi companies and many free floating
        sharing companies.
    :ivar route_description: Descriptive text for a route, f.e. "Airport
        via City Centre"
    :ivar via: Via points of the service that may help identify the
        vehicle to the public.
    :ivar attribute: Note or service attribute.
    :ivar extension:
    """
    class Meta:
        name = "BookingPTLegStructure"

    pick_up_location: Optional[ProvisionedCallAtPlaceStructure] = field(
        default=None,
        metadata={
            "name": "PickUpLocation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    set_down_location: Optional[ProvisionedCallAtPlaceStructure] = field(
        default=None,
        metadata={
            "name": "SetDownLocation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mode: Optional[ModeStructure] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    product_category: Optional[ProductCategoryStructure2] = field(
        default=None,
        metadata={
            "name": "ProductCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    published_service_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PublishedServiceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operator_refs: Optional[OperatorRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    route_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    via: List[ServiceViaPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    attribute: List[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
