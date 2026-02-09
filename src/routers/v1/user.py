from fastapi import APIRouter, Request
from config.schemas import MemberBase, LoginUserBase, SignUpBase
from config.database import get_db, db_session
from managers.user import UserManager

router = APIRouter(
    prefix="/v1/user",
    tags=['users'],
)


@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.post("/login/{action}")
def login_user(
    request: Request,
    params: LoginUserBase, 
    action: str
):
    with db_session() as db:
        if action == "email":
            return UserManager(request).login_user(db, params)
        elif action == "mobile":
            return {"response": "login by mobile"}
        elif action == "password":
            return {"response": "login by mobile"}
        
@router.post("/signup/{action}")
def singup(
    request: Request,
    params: SignUpBase, 
    action: str
):
    with db_session() as db:
        if action == "email":
            return UserManager(request).signup_via_email(db, params)
        elif action == "mobile":
            return {"response": "login by mobile"}
        elif action == "password":
            return {"response": "login by mobile"}
        
@router.post("/check")
def check(
    request: Request,
):
    with db_session() as db:
        return UserManager(request).check()
            
        