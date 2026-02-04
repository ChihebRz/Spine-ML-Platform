from pydantic import BaseModel
from typing import List

class PredictionResponse(BaseModel):
    class_name: str
    confidence: float                # still the max one
    probabilities: List[float]       # NEW: [p_normal, p_hernia, p_spondy]