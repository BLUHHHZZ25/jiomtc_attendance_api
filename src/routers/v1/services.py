from fastapi import APIRouter, Request
from config.schemas import ServiceBase
from config.database import get_db, db_session
from managers.services import ServicesManager 

router = APIRouter(
    prefix="/v1/services",
    tags=['services'],
)


@router.post("/create")
def memeber_create(
    request: Request,
    params: ServiceBase, 
):
    with db_session() as db:
        return ServicesManager(request).create(db, params)

@router.put("/update")
def memeber_create(
    request: Request,
    params: ServiceBase, 
):
    with db_session() as db:
        return ServicesManager(request).update(db, params)
        