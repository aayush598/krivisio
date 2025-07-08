from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from utils.folder_structure import generate_directory_structure

router = APIRouter()

# Reuse output schema from Tool 1
class IdeationOutput(BaseModel):
    suggested_features: str
    suggested_tech_stack: str
    total_repos_processed: int

class FolderStructureInputFromTool1(IdeationOutput):
    project_idea: str
    preferences: Optional[str] = ""

@router.post("/generate/folder-structure", tags=["Folder Structure"])
def generate_folder_structure_from_tool1(data: FolderStructureInputFromTool1):
    try:
        # Convert suggested_tech_stack from string to list
        tech_stack_list = [tech.strip() for tech in data.suggested_tech_stack.split(",") if tech.strip()]

        folder_structure = generate_directory_structure(
            project_desc=data.project_idea,
            tech_stack=tech_stack_list,
            preferences=data.preferences
        )

        return {
            "folder_structure": folder_structure,
            "project_idea": data.project_idea,
            "suggested_features": data.suggested_features,
            "total_repos_processed": data.total_repos_processed
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
