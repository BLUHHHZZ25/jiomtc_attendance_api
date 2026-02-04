from fastapi import APIRouter


router = APIRouter(
    prefix="/v1/user",
    tags=['users'],
)


@router.get("/")
def get_users():
    return {"message": "List of users"}