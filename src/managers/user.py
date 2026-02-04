from services.user import UserService
from config.log import logger as fastapi_logger
class UserManager:
    def __init__(self, request):
        self.request = request
        
    def login_user(self, db, params):
        account = UserService.get(db, {"email":params.email, "action_type":"BY_EMAIL"})
        fastapi_logger.info(f"User login attempt: {account} type {type(account)}")

        return {"response": ""}