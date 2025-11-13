from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class EmissionCo2Structure:
    """
    Estimation of CO2 emissions.

    :ivar kilogram_per_person_km: Kilograms of CO2 emission by person
        and by kilometre.
    :ivar confidence_level: Confidence level of the emission value in
        percent.
    """

    class Meta:
        name = "EmissionCO2Structure"

    kilogram_per_person_km: Optional[float] = field(
        default=None,
        metadata={
            "name": "KilogramPerPersonKm",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    confidence_level: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConfidenceLevel",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("100.0"),
        },
    )
