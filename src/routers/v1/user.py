from fastapi import APIRouter, Request
from config.schemas import MemberBase, LoginUserBase
from config.database import get_db, db_session
from managers.user import UserManager

router = APIRouter(
    prefix="/v1/user",
    tags=['users'],
)


@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.post("/login/{action}/{role}")
def login_user(
    request: Request,
    params: LoginUserBase, 
    action: str, 
    role: str
):
    with db_session() as db:
        if action == "BY_EMAIL":
            return UserManager(request).login_user(db, params)
        elif action == "BY_MOBILE":
            return {"response": "login by mobile"}
        elif action == "BY_PASSWORD":
            return {"response": "login by mobile"}
            
        