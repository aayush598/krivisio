from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_USERNAME or not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_USERNAME and GITHUB_TOKEN must be set in .env")

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

@router.post("/tool4/upload-to-github", tags=["GitHub Uploader"])
def upload_to_github(data: GitHubUploadInput):
    try:
        payload = {
            "name": data.name,
            "structure": [item.dict() for item in data.structure],
            "github_data": {
                "repo_name": data.name,
                "github_token": GITHUB_TOKEN,
                "github_username": GITHUB_USERNAME
            }
        }

        response = requests.post(
            "https://krivisio-githubcodeuploader-hfyr.onrender.com/create-and-upload",
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
