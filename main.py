from fastapi import FastAPI
from tool1_feature_suggestion import router as suggest_router
from tool1_feature_classification import router as classify_router
from tool2_cocomo2_parameters import router as cocomo_param_router

app = FastAPI()

app.include_router(suggest_router, prefix="/api")
app.include_router(classify_router, prefix="/api")
app.include_router(cocomo_param_router, prefix="/api")