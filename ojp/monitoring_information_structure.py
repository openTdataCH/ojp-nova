from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.extensions_1 import Extensions1
from ojp.monitoring_type_enumeration import MonitoringTypeEnumeration
from ojp.monitoring_validity_condition_structure import MonitoringValidityConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoringInformationStructure:
    """
    Allowed values for the monitoring conditions (frequency of mesurement, etc): an
    automatic monitoring of the satus of a lift with pushed alert in case of
    incident is very different from a daily manual/visual check.

    :ivar monitoring_interval: Mean time interval between two
        measurements.
    :ivar monitoring_type: How monitoring is automatic, manual, etc..
    :ivar monitoring_period: When the monitoring is in effect. If absent
        always.
    :ivar extensions:
    """
    monitoring_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MonitoringInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    monitoring_type: Optional[MonitoringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MonitoringType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    monitoring_period: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
