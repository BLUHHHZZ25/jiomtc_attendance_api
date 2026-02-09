from fastapi import APIRouter, Request
from config.schemas import MemberBase, LoginUserBase, SignUpBase
from config.database import get_db, db_session
from managers.members import MembersManager 

router = APIRouter(
    prefix="/v1/member",
    tags=['members'],
)


@router.post("/create")
def login_user(
    request: Request,
    params: LoginUserBase, 
    action: str
):
    with db_session() as db:
        return MembersManager(request).create(db, params)
        