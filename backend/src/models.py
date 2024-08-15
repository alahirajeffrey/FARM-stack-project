from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
# from bson import ObjectId

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]

## menu model
class MenuModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    description: str
    price: float 

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Tuwon shinkafa and miyan kuka",
                "description": "Tasty tuwon shinkafa and miyan kuka with goat meat",
                "price": 5000.0,
            }
        },
    )

class MenuList(BaseModel):
    menus: List[MenuModel]
