# tool2_cocomo2_parameters.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from utils.cocomo_parameters_generator import generate_cocomo_parameters

router = APIRouter(prefix="/tool2/cocomo2", tags=["Tool 2 - COCOMO Parameters"])

class CocomoRequest(BaseModel):
    software: str
    level: str  # e.g., "basic", "intermediate", "advanced"
    features: List[str]

@router.post("/generate-parameters")
def generate_parameters(req: CocomoRequest):
    try:
        result = generate_cocomo_parameters(req.software, req.level, req.features)
        return result
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
