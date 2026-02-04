from pydantic import BaseModel, Field

class SpineRequest(BaseModel):
    pelvic_incidence: float
    pelvic_tilt: float
    lumbar_lordosis_angle: float
    sacral_slope: float
    pelvic_radius: float
    degree_spondylolisthesis: float
