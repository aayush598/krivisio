from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union
import requests

router = APIRouter()

# Define structure schema
class StructureItem(BaseModel):
    type: str  # "file" or "folder"
    name: str
    children: Union[List['StructureItem'], None] = None

StructureItem.update_forward_refs()

class GitHubUploadInput(BaseModel):
    name: str
    structure: List[StructureItem]
    github_username: str
    github_token: str

@router.post("/tool4/upload-to-github", tags=["GitHub Uploader"])
def upload_to_github(data: GitHubUploadInput):
    try:
        payload = {
            "name": data.name,
            "structure": [item.dict() for item in data.structure],
            "github_data": {
                "repo_name": data.name,
                "github_token": data.github_token,
                "github_username": data.github_username
            }
        }

        response = requests.post(
            "https://krivisio-githubcodeuploader.onrender.com/create-and-upload",
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        result = response.json()

        return {
            "status": "success" if result.get("success", False) else "failed",
            "message": result.get("message", "Unknown response"),
            "repo_name": data.name
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"GitHub upload failed: {str(e)}")
