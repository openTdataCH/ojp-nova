from dataclasses import dataclass, field
from typing import List
from ojp.optimisation_method_enumeration import OptimisationMethodEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OptimisationMethodList:
    """List of OptimisationMethods.

    The order of precedence - if used at all - is high to low. In single criteria optimisers the optimisation methods may be used in parallel and not truly used to score the results.
    """
    optimisation_method: List[OptimisationMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OptimisationMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
