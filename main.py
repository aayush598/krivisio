from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tool1_feature_suggestion import router as suggest_router
from tool1_feature_classification import router as classify_router
from tool2_cocomo2_parameters import router as cocomo_param_router
from tool2_cocomo2_evaluation import router as cocomo2_router
from tool2_specsheet_generator import router as specsheet_router
from tool3_folder_structure_generator import router as folder_structure_router
from tool4_github_uploader import router as github_uploader_router
from tool5_talent_matching import router as talent_matching_router

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or replace "*" with ["http://localhost:5173"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(suggest_router, prefix="/api")
app.include_router(classify_router, prefix="/api")
app.include_router(cocomo_param_router, prefix="/api")
app.include_router(cocomo2_router, prefix="/api")
app.include_router(specsheet_router, prefix="/api")
app.include_router(folder_structure_router, prefix="/api")
app.include_router(github_uploader_router, prefix="/api")
app.include_router(talent_matching_router, prefix="/api")