from fastapi import FastAPI
from router import router

app = FastAPI(
    title="FARM Stack Menu API", 
    summary="Backend for fullstack menu application using FastApi, React and Mongodb"
    )

app.include_router(router=router, prefix="/api/v1/menu", tags=["menu"])


@app.get("/")
async def root():
    return {"message": "Backend server running"} 