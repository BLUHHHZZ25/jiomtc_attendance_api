from config.crud import MemberGroup


class MemberGroupsService:
    @staticmethod
    def get(db, params):
        return MemberGroup.get(db, params)
    
    @staticmethod
    def create(db, params):
        return MemberGroup.create(db, params)
    
    @staticmethod
    def update(db, params):
        return MemberGroup.update(db, params)

    