from services.user import UserService
from config.log import logger as fastapi_logger
from utils.auth import Auth, JwtService
class UserManager:
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
    
        
    def login_user(self, db, params):
        # init_auth = self.init_auth("ACCESS_TOKEN")
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
            
            access_token = JwtService().encode({}, {"user_id": account.id, "email": account.email})
            
            refresh_token = JwtService().encode({"token_type":'REFRESH'}, {"user_id": account.id, "email": account.email})
            
            
            return {
                    "response": "200 OK",
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
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