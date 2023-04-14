from dataclasses import dataclass
from ojp.vehicle_orientation_relative_to_quay import VehicleOrientationRelativeToQuay

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalOrientationRelativeToQuay(VehicleOrientationRelativeToQuay):
    """Indication of the direction of travel of the vehicle (e.g. TRAIN formation) with respect to the platform, or more precisely the QUAY. Unbounded to allow multiple languages. (since SIRI 2.1)
    Examples:
    - "towards A" or "towards sector A" if the QUAY is separated into sub-QUAYs or so called sectors. This would be equivalent to the vehicle arriving at sector A first when approaching the QUAY with sectors A-B-C-D. If the arriving vehicle is represented as an arrow, "towards A" would be abstracted as "=&gt; A-B-C-D".
    - "towards 0" or "towards reference point 0" if sectors are not available or the QUAY has a reference point, e.g. for measuring the length of the QUAY, identified by "0". This would be equivalent to the vehicle arriving at this reference point first when approaching the QUAY. If the arriving vehicle is represented as an arrow, "towards 0" would be abstracted as "=&gt; 0...100". "100" (as in percent) could denote the opposite side of the QUAY (measured at the full length of the QUAY with respect to the reference point).
    It is advised to specify a reference point that is meaningful for passengers on location."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
