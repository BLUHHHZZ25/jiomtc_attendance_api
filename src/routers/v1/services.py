from fastapi import APIRouter, Request
from config.schemas import ServiceBase, ServiceParams
from config.database import get_db, db_session
from managers.services import ServicesManager 

router = APIRouter(
    prefix="/v1/services",
    tags=['services'],
)

@router.get("/get")
def service_create(
    request: Request,
    params: ServiceParams, 
):
    with db_session() as db:
        return ServicesManager(request).get(db, params)
    
@router.post("/create")
def service_create(
    request: Request,
    params: ServiceBase, 
):
    with db_session() as db:
        return ServicesManager(request).create(db, params)

@router.put("/update")
def service_update(
    request: Request,
    params: ServiceBase, 
):
    with db_session() as db:
        return ServicesManager(request).update(db, params)
        