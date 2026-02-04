from config import models
from config.log import logger as fastapi_logger
class User:
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_EMAIL':
                    return db.query(models.User).filter(models.User.email == params['email']).filter(models.User.is_active == True).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"User.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_user = models.User(
                username=params.username,
                email=params.email,
                password_hash=params.password_hash,
                full_name=params.full_name,
                role=params.role
            )
            db.add(create_user)
            db.commit()
            db.refresh(create_user)
            
            return 
        except Exception as ex:
            fastapi_logger.error(f"User.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

        
    def put(db, params):
        try:
            return {"response"}
        except Exception as ex:
            fastapi_logger.error(f"User.put is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

    def delete(db, params):
        try:
            return {"response"}
        except Exception as ex:
            fastapi_logger.error(f"User.delete is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")
