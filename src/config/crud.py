from config import models

class User:
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_EMAIL':
                    return db.query(models.User).filter(models.user.email == params['email']).filter(models.user.is_active == True).first()
            return {"response"}
        except Exception as e:
            raise Exception(f"DB Error: {str(e)}")
        
    def create(db, params):
        try:
            return {"response"}
        except Exception as e:
            raise Exception(f"DB Error: {str(e)}")
        
    def put(db, params):
        try:
            return {"response"}
        except Exception as e:
            raise Exception(f"DB Error: {str(e)}")

    def delete(db, params):
        try:
            return {"response"}
        except Exception as e:
            raise Exception(f"DB Error: {str(e)}")