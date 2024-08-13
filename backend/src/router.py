from fastapi import APIRouter, status, HTTPException, Body, Response
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
    return Response(status_code=status.HTTP_201_CREATED, content=created_menu)


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
        return Response(content=menu_exists, status_code=status.HTTP_200_OK)
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
    menu_list= MenuList(menus= await menu_collection.find().to_list(100))
    return Response(content=menu_list, status_code=status.HTTP_200_OK)


@router.delete("/menu/{id}", response_description="Delete a menu")
async def delete_menu_item(id: str):
    """
    Delete a single menu from the database.
    """
    delete_result = await menu_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_200_OK, content="menu deleted")
    
    raise HTTPException(status_code=404, detail="menu not found")