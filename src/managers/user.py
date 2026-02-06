from services.user import UserService
from config.log import logger as fastapi_logger
class UserManager:
    def __init__(self, request):
        self.request = request
        
    def login_user(self, db, params):
        try:
            account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})
            account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})
            if account is None:
                fastapi_logger.info(f"User Login Failed: No account found for email {params.email}")
                return {"response": "Invalid email or password"}
            
            if account.is_active == False:
                fastapi_logger.info(f"User Login Failed: Account is not active {params.email}")
                return {"response": "Account is not active"}

            return {"response": ""}
        except Exception as ex:
            fastapi_logger.error(f"UserManager.login_user is failed: {str(ex)} - email: {params.email}")
            raise Exception(f"Login Error: {str(ex)}")
        
    def signup_via_email(self, db, params):
        try:
            account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})
            account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})
            if account is None:
                fastapi_logger.info(f"User Login Failed: No account found for email {params.email}")
                return {"response": "Invalid email or password"}
            
            if account.is_active == False:
                fastapi_logger.info(f"User Login Failed: Account is not active {params.email}")
                return {"response": "Account is not active"}

            return {"response": ""}
        except Exception as ex:
            fastapi_logger.error(f"UserManager.login_user is failed: {str(ex)} - email: {params.email}")
            raise Exception(f"Login Error: {str(ex)}")