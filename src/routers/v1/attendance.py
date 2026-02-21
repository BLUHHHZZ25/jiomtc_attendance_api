from fastapi import APIRouter


router = APIRouter(
    prefix="/v1/attendance",
    tags=['attendance'],
)


# @router.get("/")
# def get_users():
#     return {"message": "List of attendance records"}