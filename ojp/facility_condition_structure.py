from dataclasses import dataclass, field
from typing import Optional
from ojp.extensions_1 import Extensions1
from ojp.facility_status_structure import FacilityStatusStructure
from ojp.facility_structure import FacilityStructure
from ojp.half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from ojp.monitoring_information_structure import MonitoringInformationStructure
from ojp.remedy_structure import RemedyStructure
from ojp.situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityConditionStructure:
    """
    Description of any change concerning a MONITORED FACILITY New structure defined
    in SIRI XSD 1.1 for Faclities Management.

    :ivar facility: Facility affected by condition.
    :ivar facility_ref:
    :ivar facility_status: Status of Facility.
    :ivar situation_ref:
    :ivar remedy: Setup action to remedy the change of the facility
        status (if partialy or totaly anavailable)
    :ivar monitoring_info: Description of the mechanism used to monitor
        the change of the facility status.
    :ivar validity_period: Period (duration) of the status change for
        the facility.
    :ivar extensions:
    """
    facility: Optional[FacilityStructure] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_status: Optional[FacilityStatusStructure] = field(
        default=None,
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    remedy: Optional[RemedyStructure] = field(
        default=None,
        metadata={
            "name": "Remedy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    monitoring_info: Optional[MonitoringInformationStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringInfo",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    validity_period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
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
