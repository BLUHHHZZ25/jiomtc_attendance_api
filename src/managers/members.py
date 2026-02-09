
from fastapi import HTTPException
from utils.auth import Auth, JwtService
from config.log import logger as fastapi_logger
from services.member import MembersService

class MembersManager:
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
    
    def create(self, db, params):
        try:
            member_data = MembersService().get(db, {"email":params.email, "action_type": "BY_EMAIL"})
            
            
            if member_data and member_data.email == params.email:
                fastapi_logger.info(f"Member Creation Failed: Emails is Already Exists {params.email}")
                raise Exception(f"Email is Already Exists", status_code=400)
            
            if member_data and member_data.phone == params.phone:
                fastapi_logger.info(f"Member Creation Failed: Phone Number is Already Exists {params.email}")
                raise Exception(f"Phone Number is Already Exists", status_code=400)
                
            create_memeber = MembersService().create(db, {
                    "name": params.name,
                    "email": params.email,
                    "phone": params.phone,
                    "join_date": params.join_date,
                    "status": params.status,
                    "address": params.address,
                    "date_of_birth": params.date_of_birth,
                    "gender": params.gender,
                    "emergency_contact_name": params.emergency_contact_name,
                    "emergency_contact_phone": params.emergency_contact_phone,
                    "notes": params.notes
            })
            
             
            return {
                    "response": "200",
                    "message": "Member Created Successfully",
                    "memeber_id": create_memeber.id
            }
        except Exception as ex:
            fastapi_logger.error(f"MemberManager.create is failed: {str(ex)} ")
            raise Exception(f"Login Error: {str(ex)}")
        
        
    def update(self, db, params):
        member_data = MembersService().get(db, {"email":params.email, "action_type": "BY_EMAIL"})
        
        if not member_data:
            fastapi_logger.info(f"Member Update Failed: Emails is not existing {params.email}")
            raise HTTPException(detail="Email is Already Exists", status_code=400)

        try:
                
            update_member = MembersService().update(db, {
                    "action_type": "UPDATE_PROFILE",
                    "name": params.name,
                    "email": params.email,
                    "phone": params.phone,
                    "join_date": params.join_date,
                    "status": params.status,
                    "address": params.address,
                    "date_of_birth": params.date_of_birth,
                    "gender": params.gender,
                    "emergency_contact_name": params.emergency_contact_name,
                    "emergency_contact_phone": params.emergency_contact_phone,
                    "notes": params.notes
            })
            
             
            return {
                    "response": "200",
                    "message": "Member Updated Successfully",
                    "memeber_id": update_member.id
            }
        except Exception as ex:
            fastapi_logger.error(f"MemberManager.login_user is failed: {str(ex)} ")
            raise Exception(f"Login Error: {str(ex)}")
