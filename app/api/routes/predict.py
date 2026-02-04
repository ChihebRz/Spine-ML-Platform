from fastapi import APIRouter
from app.schemas.request import SpineRequest
from app.schemas.response import PredictionResponse
from app.services.inference import predict

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def make_prediction(req: SpineRequest):

    data = [
        req.pelvic_incidence,
        req.pelvic_tilt,
        req.lumbar_lordosis_angle,
        req.sacral_slope,
        req.pelvic_radius,
        req.degree_spondylolisthesis
    ]

    return predict(data)
