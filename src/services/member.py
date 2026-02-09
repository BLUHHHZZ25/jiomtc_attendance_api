from config.crud import Member


class MembersService:
    @staticmethod
    def get(db, params):
        return Member.get(db, params)
    
    @staticmethod
    def create(db, params):
        return Member.create(db, params)
    
    @staticmethod
    def update(db, params):
        return Member.update(db, params)

    