
from fastapi import HTTPException
from utils.auth import Auth, JwtService
from config.log import logger as fastapi_logger
from services.services import ServicesService 

class ServicesManager:
    def __init__(self, request):
        self.request = request
        
    def init_auth(self, type):
        app_info = {
            'authorized': False
        }
        if( type == "ACCESS_TOKEN"):
            app_info=Auth(self.request).validate_token()
        else:
            app_info= Auth(self.request).validate_signup()
            
        return app_info
    
    def get(self, db, params):
        if not params.action:
            fastapi_logger.info(f"Service Get Failed: Params Action is Null")
            raise HTTPException(detail="Params Action is null", status_code=500)
        
        if params.action == "BY_SERVICE_NAME":
            member_data = ServicesService().get(db, {"action_type": "BY_EMAIL", "email": params.service_name})
        elif params.action == "BY_ID":
            member_data = ServicesService().get(db, {"action_type": "BY_ID"})
        elif params.action == "BY_ALL":
            member_data = ServicesService().get(db, {"action_type": "BY_ALL"})

        if not member_data:
            fastapi_logger.info(f"Services not fount")
            raise HTTPException(detail="Services not found", status_code=404)
        try:
             
            return {
                    "response": "200",
                    "message": "Services Get Successfully",
                    "data": member_data
            }
        
        except Exception as ex:
            fastapi_logger.error(f"ServiceManager.get is failed: {str(ex)} ")
            raise Exception(f"Service Manager.get Error: {str(ex)}")

    def create(self, db, params):
        services_data = ServicesService().get(db, {"service_name":params.service_name, "action_type": "BY_SERVICE_NAME"})
        
        if services_data and services_data.service_name == params.service_name:
            fastapi_logger.info(f"Services Creation Failed: Services is Already Exists {params.service_name}")
            raise HTTPException(detail="Service is Already Exists", status_code=400)
        try:
                
            create_memeber = ServicesService().create(db, {
                "service_name": params.service_name,
                "service_type": params.service_type,
                "description": params.description,
                "default_day_of_week": params.default_day_of_week,
                "default_time": params.default_time,
                "is_active": params.is_active
            })
            
             
            return {
                    "response": "200",
                    "message": "Service Created Successfully",
                    "memeber_id": create_memeber.id
            }
        except Exception as ex:
            fastapi_logger.error(f"ServicesManager.create is failed: {str(ex)} ")
            raise Exception(f"ServicesManager Error: {str(ex)}")
        
        
    def update(self, db, params):
        services_data = ServicesService().get(db, {"service_name":params.service_name, "action_type": "BY_SERVICE_NAME"})
        
        if not services_data:
            fastapi_logger.info(f"Service Update Failed: Services is not existing {params.service_name}")
            raise HTTPException(detail="Services is not Exists", status_code=400)

        try:
                
            update_member = ServicesService().update(db, {
                    "action_type": "UPDATE_SERVICES",
                    "service_name": params.service_name,
                    "service_type": params.service_type,
                    "description": params.description,
                    "default_day_of_week": params.default_day_of_week,
                    "default_time": params.default_time,
                    "is_active": params.is_active
            })
            
             
            return {
                    "response": "200",
                    "message": "Services Updated Successfully",
            }
        except Exception as ex:
            fastapi_logger.error(f"ServiceManager.login_user is failed: {str(ex)} ")
            raise Exception(f"ServiceManager Error: {str(ex)}")
