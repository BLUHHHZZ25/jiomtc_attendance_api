from config.crud import AttendanceRecord


class AttendanceRecordsService:
    @staticmethod
    def get(db, params):
        return AttendanceRecord.get(db, params)
    
    @staticmethod
    def create(db, params):
        return AttendanceRecord.create(db, params)
    
    @staticmethod
    def update(db, params):
        return AttendanceRecord.update(db, params)

    