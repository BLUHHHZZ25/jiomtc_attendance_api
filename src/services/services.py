from config.crud import Services


class ServicesService:
    @staticmethod
    def get(db, params):
        return Services.get(db, params)
    
    @staticmethod
    def create(db, params):
        return Services.create(db, params)
    
    @staticmethod
    def update(db, params):
        return Services.update(db, params)

    