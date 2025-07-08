from fastapi import FastAPI
from tool1_feature_suggestion import router as tool1_router

app = FastAPI()
app.include_router(tool1_router, prefix="/api")
