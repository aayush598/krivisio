from fastapi import FastAPI
from tool1_feature_suggestion import router as suggest_router
from tool1_feature_classification import router as classify_router

app = FastAPI()

app.include_router(suggest_router, prefix="/api")
app.include_router(classify_router, prefix="/api")
