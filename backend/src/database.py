import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values(".env")

client = motor.motor_asyncio.AsyncIOMotorClient(config["MONGO_URI"])
db = client.sholly
menu_collection = db.get_collection("menu")
