from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.quality_index_enumeration import QualityIndexEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PredictionQualityStructure:
    """
    Type for Prediction Quality quantifcation.

    :ivar prediction_level: An approxiimate characterisation of
        prediction quality as one of five values . +SIRI v2.0
    :ivar percentile: Percentile associated with range as specified by
        lower and upper bound +SIRI v2.0
    :ivar lower_time_limit: Lower bound on time of for prediction  for
        confidence level if different from defaults  +SIRI v2.0
    :ivar higher_time_limit: Upper bound on time of for predictios  for
        confidence level if different from defaults  +SIRI v2.0
    """
    prediction_level: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "PredictionLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    percentile: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    lower_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LowerTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    higher_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HigherTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
