# tool2_cocomo2_evaluation.py

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, Any
from utils.cocomo2_evaluator import evaluate_cocomo2

router = APIRouter()

class Cocomo2Input(BaseModel):
    function_points: Dict[str, Any]
    reuse: Dict[str, Any]
    revl: Dict[str, Any]
    effort_schedule: Dict[str, Any]

@router.post("/tool2/cocomo2_evaluation")
async def cocomo2_evaluation(request: Request, input_data: Cocomo2Input):
    try:
        results = evaluate_cocomo2(input_data.dict())
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
