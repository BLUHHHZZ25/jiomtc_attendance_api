from config.crud import AttendanceSession


class AttendanceSessionsService:
    @staticmethod
    def get(db, params):
        return AttendanceSession.get(db, params)
    
    @staticmethod
    def create(db, params):
        return AttendanceSession.create(db, params)
    
    @staticmethod
    def update(db, params):
        return AttendanceSession.update(db, params)

    