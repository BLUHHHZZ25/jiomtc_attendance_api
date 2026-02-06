from config.crud import User


class UserService:
    @staticmethod
    def get(db, params):
        return User.get(db, params)
    
    @staticmethod
    def create(db, params):
        return User.create(db, params)
    
    @staticmethod
    def post(db, params):
        return User.post(db, params)