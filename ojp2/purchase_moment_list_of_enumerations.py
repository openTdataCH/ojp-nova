from dataclasses import dataclass, field

from ojp2.purchase_moment_enumeration import PurchaseMomentEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PurchaseMomentListOfEnumerations:
    """
    List of Purchase Moment values.

    :ivar purchase_moment: Possibilities when to pay.
    """

    purchase_moment: list[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
