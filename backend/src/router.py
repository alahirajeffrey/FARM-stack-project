from fastapi import APIRouter, status, Depends, HTTPException
from database import menu_collection
from models import MenuModel, MenuList

router = APIRouter()

# @router.post(
#     "/menu/",
#     response_description="Add new menu",
#     response_model=MenuModel,
#     status_code=status.HTTP_201_CREATED,
#     response_model_by_alias=False,
# )
async def add_menu_item():
    pass

async def get_single_menu_item():
    pass

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