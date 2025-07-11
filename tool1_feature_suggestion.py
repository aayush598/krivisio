import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Input schema
class IdeationInput(BaseModel):
    project_idea: str
    max_repos: int

# Output schema
class IdeationOutput(BaseModel):
    suggested_features: str
    suggested_tech_stack: str
    total_repos_processed: int

# POST endpoint to fetch feature suggestions via Tool 1
@router.post("/tool1/suggest", response_model=IdeationOutput)
def suggest_features_and_stack(input: IdeationInput):
    try:
        print(f"inpu : {input}")
        response = requests.post(
            "https://github-project-extractor-4v1r.onrender.com/ideate",
            json=input.dict(),
            timeout=60
        )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch data from Tool 1")

        data = response.json()

        return {
            "suggested_features": data.get("suggested_features", ""),
            "suggested_tech_stack": data.get("suggested_tech_stack", ""),
            "total_repos_processed": data.get("total_repos_processed", 0)
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
