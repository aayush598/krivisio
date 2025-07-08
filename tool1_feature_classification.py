from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.groq_utils import generate_feature_sets

router = APIRouter()

# Request schema
class FeatureClassificationInput(BaseModel):
    project_idea: str
    suggested_features_text: str

# Response schema
class FeatureClassificationOutput(BaseModel):
    basic: list[str]
    intermediate: list[str]
    advanced: list[str]

@router.post("/tool1/classify-features", response_model=FeatureClassificationOutput)
def classify_features(data: FeatureClassificationInput):
    try:
        result = generate_feature_sets(data.project_idea, data.suggested_features_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
