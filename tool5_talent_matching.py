from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.talent_matching import match_talent_profiles
from typing import Dict, Any
import json
router = APIRouter()


@router.post("/match/talent", tags=["Talent Matching"])
def get_matched_talent(data: Dict[str, Any]):
    try:
        response = match_talent_profiles(data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

