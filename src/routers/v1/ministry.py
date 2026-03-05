from fastapi import APIRouter, Request
from config.schemas import MemberBase, LoginUserBase, MemberGet, SignUpBase
from config.database import get_db, db_session
from managers.members import MembersManager 

router = APIRouter(
    prefix="/v1/ministry",
    tags=['ministry'],
)

@router.get("/")
def get_ministy():
    return {"message": "List of ministry"}

@router.get("/get")
def memeber_get(
    request: Request,
    params: MemberGet
):
    with db_session() as db:
        return MembersManager(request).get(db,params)
    
@router.post("/create")
def memeber_create(
    request: Request,
    params: MemberBase, 
):
    with db_session() as db:
        return MembersManager(request).create(db, params)

@router.put("/update")
def member_update(
    request: Request,
    params: MemberBase, 
):
    with db_session() as db:
        return MembersManager(request).update(db, params)
        