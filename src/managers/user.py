

class UserManager:
    def __init__(self, request):
        self.request = request
        
    def login_user(self, db, params):
        return {"response": "login params"}