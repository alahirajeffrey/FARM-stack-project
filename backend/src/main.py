from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()

## connect to database on server startup
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB!")

## disconnect mongodb connection
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Connection to the MongoDB closed!")

## root 
@app.get("/")
async def root():
    return {"message": "Welcome!"}