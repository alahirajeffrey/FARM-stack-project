from fastapi import FastAPI
import router as menu_router

app = FastAPI(
    title="FARM Stack Menu API", 
    summary="Backend for fullstack menu application using FastApi, React and Mongodb"
    )

app.include_router(menu_router, prefix="/api/v1", tags=["menu"])
