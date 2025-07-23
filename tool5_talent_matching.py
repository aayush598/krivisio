from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from utils.talent_matching import match_talent_profiles

router = APIRouter()

class TalentMatchingRequest(BaseModel):
    tech_stack: str
    avg_team_size: float
    manager_score_threshold: float

@router.post("/match/talent", tags=["Talent Matching"])
def get_matched_talent(data: TalentMatchingRequest):
    try:
        response = match_talent_profiles(
            tech_stack=data.tech_stack,
            avg_team_size=data.avg_team_size,
            manager_score_threshold=data.manager_score_threshold
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
