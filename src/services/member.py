from config.crud import User


class MembersService:
    @staticmethod
    def get(db, params):
        return User.get(db, params)

    