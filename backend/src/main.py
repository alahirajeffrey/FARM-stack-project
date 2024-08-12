from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    ## connect to database on server startup
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB!")

    yield

    ## disconnect mongodb connection
    app.mongodb_client.close()
    print("Connection to the MongoDB closed!")


app = FastAPI(lifespan=lifespan)


## root 
@app.get("/")
async def root():
    return {"message": "Welcome!"}