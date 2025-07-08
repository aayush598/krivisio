from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from utils.specsheet_generator import build_comprehensive_spec_sheet

router = APIRouter()

class SpecSheetInput(BaseModel):
    software: str
    level: str
    features: List[str]
    api_results: Dict[str, Any]

@router.post("/generate/specsheet", tags=["Specification Sheet"])
def generate_specsheet(data: SpecSheetInput):
    try:
        result = build_comprehensive_spec_sheet(
            software=data.software,
            level=data.level,
            features=data.features,
            api_results=data.api_results
        )
        return {"specsheet": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
