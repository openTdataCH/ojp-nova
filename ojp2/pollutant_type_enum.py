from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class PollutantTypeEnum(Enum):
    BENZENE_TOLUENE_XYLENE = "benzeneTolueneXylene"
    CARBON_MONOXIDE = "carbonMonoxide"
    LEAD = "lead"
    METHANE = "methane"
    NITRIC_OXIDE = "nitricOxide"
    NITROGEN_DIOXIDE = "nitrogenDioxide"
    NITROGEN_MONOXIDE = "nitrogenMonoxide"
    NITROGEN_OXIDES = "nitrogenOxides"
    NON_METHANE_HYDROCARBONS = "nonMethaneHydrocarbons"
    OZONE = "ozone"
    PARTICULATES10 = "particulates10"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "polycyclicAromaticHydrocarbons"
    PRIMARY_PARTICULATE = "primaryParticulate"
    SULPHUR_DIOXIDE = "sulphurDioxide"
    TOTAL_HYDROCARBONS = "totalHydrocarbons"
