from fastapi import APIRouter, status, Depends, HTTPException, Body
from database import menu_collection
from models import MenuModel, MenuList
from bson import ObjectId

router = APIRouter()

@router.post(
    "/menu/",
    response_description="Add new menu",
    response_model=MenuModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def add_menu_item(menu: MenuModel = Body(...)):
    """
    Insert a new menu into the databas.

    A unique `id` will be created and provided in the response.
    """
    new_menu = await menu_collection.insert_one(
        menu.model_dump(by_alias=True, exclude=["id"])
    )

    created_menu = await menu_collection.find_one(
         {"_id": new_menu.inserted_id}
    )
    return created_menu


@router.get(
    "/menu/{id}",
    response_description="Get menu by id",
    response_model=MenuModel,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def get_single_menu_item(id: str):
    """
    Get single menu by `id`.
    """
    menu_exists = await menu_collection.find_one({"_id": ObjectId(id)})
    if menu_exists is not None:
        return menu_exists
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu does not exist")


@router.get(
    "/menus/",
    response_description="List all menus",
    response_model=MenuModel,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def get_all_menu_items():
    """
    List all of the menus in the database.

    The response is unpaginated and limited to 100 results.
    """
    return MenuList(menus= await menu_collection.find().to_list(100))


async def delete_menu_item():
    pass