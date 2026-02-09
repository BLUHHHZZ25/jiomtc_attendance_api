from config.crud import MemberGroupAssignment


class MemberGroupAssignmentsService:
    @staticmethod
    def get(db, params):
        return MemberGroupAssignment.get(db, params)
    
    @staticmethod
    def create(db, params):
        return MemberGroupAssignment.create(db, params)
    
    @staticmethod
    def update(db, params):
        return MemberGroupAssignment.update(db, params)

    