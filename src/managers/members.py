
from utils.auth import Auth, JwtService
from config.log import logger as fastapi_logger

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
            return {"response": {}}
        except Exception as ex:
            fastapi_logger.error(f"UserManager.login_user is failed: {str(ex)} ")
            raise Exception(f"Login Error: {str(ex)}")
