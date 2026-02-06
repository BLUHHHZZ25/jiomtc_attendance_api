from services.user import UserService
from config.log import logger as fastapi_logger
from utils.auth import Auth
class UserManager:
    def __init__(self, request):
        self.request = request
        
    def login_user(self, db, params):
        try:
            account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})

            if account is None:
                fastapi_logger.info(f"User Login Failed: No account found for email {params.email}")
                return {"response": "Invalid email or password"}
            
            if account.is_active == False:
                fastapi_logger.info(f"User Login Failed: Account is not active {params.email}")
                return {"response": "Account is not active"}
            
            if not account or not Auth.verify_password(params.password, account.password_hash):
                fastapi_logger.info(f"User Login Failed: Incorrect password for email {params.email}")
                return {"response": "Invalid email or password"}
            return {"response": "200 OK"}
        except Exception as ex:
            fastapi_logger.error(f"UserManager.login_user is failed: {str(ex)} - email: {params.email}")
            raise Exception(f"Login Error: {str(ex)}")
        
    def signup_via_email(self, db, params):
        try:
            fastapi_logger.info(f"password {Auth.get_hashed_password(params.password)}")
            account = UserService.create(db, {
                "username": params.username,
                "email": params.email,
                "password": Auth.get_hashed_password(params.password),
                "full_name": params.full_name,
                "role": params.role
            })
            
            

            return {"response": account}
        except Exception as ex:
            fastapi_logger.error(f"UserManager.signup_via_email is failed: {str(ex)} - email: {params.email}")
            raise Exception(f"Login Error: {str(ex)}")