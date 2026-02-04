from fastapi import HTTPException, status
import random
import uuid
import bcrypt
from datetime import datetime

from config_setting import setting
from config.log import logger as fastapi_logger
from config import constant
from services.jwt import JwtService
from google.oauth2 import id_token
from google.auth.transport import requests  

class Auth:
    def __init__(self, request=None):
        self.request = request

    @staticmethod
    def generate_random(type, count=16):
        if type == "alphanumeric":
            characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif type == "numeric":
            characters = "0123456789"
        elif type == "alphabet":
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif type == "uuid":
            return f"{uuid.uuid4()}"

        return "".join(random.choice(characters) for _ in range(count))

    def generate_username(self, phone_number):
        utc_now = datetime.utcnow()
        mid_digits = self.generate_random("numeric", 3)
        last_digits = phone_number[-4:]
        
        return f"ra{utc_now.strftime('%Y%m%d%H%M%S')}{mid_digits}{last_digits}"
    
    def generate_username_email(self, email):
        utc_now = datetime.utcnow()
        mid_digits = self.generate_random("numeric", 3)
        local_part = email.split("@")[0][:5] # Take first 5 chars before "@"
        
        return f"ra{utc_now.strftime('%Y%m%d%H%M%S')}{mid_digits}{local_part}"

    @staticmethod
    def get_hashed_password(password):
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=password_bytes, salt=salt)
        return hashed_password

    @staticmethod
    def verify_password(password, hashed_password):
        password_bytes = password.encode('utf-8')
        hashed_password = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password=password_bytes, hashed_password=hashed_password)

    def validate_signup(self, type):
        authorized = False

        try:
            app_name = self.request.headers.get("z-app")
            app_type = self.request.headers.get("z-app-type")
            app_version = self.request.headers.get("z-app-version")
            app_code = self.request.headers.get("z-app-code")

            client_host = self.request.client.host
            forwarded_for = self.request.headers.get("X-Forwarded-For")
            real_ip = self.request.headers.get("X-Real-IP")
            client_ip = forwarded_for or real_ip or client_host
            uuid = None
            authorization = None
            decoded_jwt = None

            if not app_name or not app_type or not app_version or not app_code or not client_ip:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

            if type == constant.AccountStatus.INITIAL.value:
                app_key = self.request.headers.get("z-app-key")
                app_secret = self.request.headers.get("z-app-secret")
                uuid = self.request.headers.get("uuid") # signup_id

                if app_key != setting.APP_KEY_RAPIDOO_SUPERAPP or app_secret != setting.APP_SECRET_RAPIDOO_SUPERAPP:
                    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
                    
                authorized = True

            elif type == constant.AccountStatus.FOR_OTP.value:
                uuid = self.request.headers.get("uuid") # account_signup.token
                authorized = True

            elif type == constant.AccountStatus.VERIFIED.value:
                authorization = self.request.headers.get("Authorization") # signup_token
                uuid = self.request.headers.get("uuid") # signup_id
                if authorization.startswith('Bearer '):
                    jwt_token = authorization[7:]
                    
                    decoded_jwt = JwtService().decode({
                        "token_type": "SIGNUP",
                        "token": jwt_token
                    })
                    authorized = True
                    
                    
            elif type in [constant.AccountStatus.NEW.value, constant.AccountStatus.REGISTERED.value]:
                uuid = self.request.headers.get("uuid")
                app_name= self.request.headers.get("z-app")
                authorized = True
                
            return {
                "authorized": authorized,
                "app_name": app_name,
                "app_type": app_type,
                "app_version": app_version,
                "app_code": app_code,
                "client_ip": client_ip,
                "uuid": uuid,
                "authorization": authorization,
                "decoded_jwt": decoded_jwt
            }
        except Exception as ex:
            fastapi_logger.error(f"Auth.validate_signup: {str(ex)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    def validate_signin(self):
        authorized = False

        try:
            app_name = self.request.headers.get("z-app")
            app_type = self.request.headers.get("z-app-type")
            app_version = self.request.headers.get("z-app-version")
            app_code = self.request.headers.get("z-app-code")
            app_key = self.request.headers.get("z-app-key")
            app_secret = self.request.headers.get("z-app-secret")
            uuid = self.request.headers.get("uuid") # device_id

            client_host = self.request.client.host
            forwarded_for = self.request.headers.get("X-Forwarded-For")
            real_ip = self.request.headers.get("X-Real-IP")
            client_ip = forwarded_for or real_ip or client_host

            if not app_name or not app_type or not app_version or not app_code or not client_ip or (app_key != setting.APP_KEY_RAPIDOO_SUPERAPP or app_secret != setting.APP_SECRET_RAPIDOO_SUPERAPP):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

            authorized = True

            return {
                "authorized": authorized,
                "app_name": app_name,
                "app_type": app_type,
                "app_version": app_version,
                "app_code": app_code,
                "client_ip": client_ip,
                "uuid": uuid
            }
        except Exception as ex:
            fastapi_logger.error(f"Auth.validate_signin: {str(ex)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    def validate_token(self):
        authorized = False

        try:
            app_name = self.request.headers.get("z-app")
            app_type = self.request.headers.get("z-app-type")
            app_version = self.request.headers.get("z-app-version")
            app_code = self.request.headers.get("z-app-code")
            app_key = self.request.headers.get("z-app-key")
            app_secret = self.request.headers.get("z-app-secret")
            uuid = self.request.headers.get("uuid") # device_id
            authorization = self.request.headers.get("Authorization")

            client_host = self.request.client.host
            forwarded_for = self.request.headers.get("X-Forwarded-For")
            real_ip = self.request.headers.get("X-Real-IP")
            client_ip = forwarded_for or real_ip or client_host
            # decoded_jwt = None


            # return "hello"
            if not app_name or not app_type or not app_version or not app_code or not client_ip or not uuid :
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorfddfized")
            
            if authorization.startswith('Bearer'):
                jwt_token = authorization[7:]
                decoded_jwt = JwtService().decode({"token": jwt_token})
                authorized = True

            authorized = True
            return {
                "authorized": authorized,
                "app_name": app_name,
                "app_type": app_type,
                "app_version": app_version,
                "app_code": app_code,
                "client_ip": client_ip,
                "uuid": uuid,
                "decoded_jwt": decoded_jwt
            }
        except Exception as ex:
            fastapi_logger.error(f"Auth.validate_token: {str(ex)}")
            # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    def validate_refresh(self):
        authorized = True

        try:
            app_name = self.request.headers.get("z-app")
            app_type = self.request.headers.get("z-app-type")
            app_version = self.request.headers.get("z-app-version")
            app_code = self.request.headers.get("z-app-code")
            uuid = self.request.headers.get("uuid") # device_id
            authorization = self.request.headers.get("Authorization") # refresh_token

            client_host = self.request.client.host
            forwarded_for = self.request.headers.get("X-Forwarded-For")
            real_ip = self.request.headers.get("X-Real-IP")
            client_ip = forwarded_for or real_ip or client_host
            decoded_jwt = None

            if not app_name or not app_type or not app_version or not app_code or not client_ip or not uuid or not authorization:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={uuid})
                # raise {f"{app_name} {app_type} {app_version} {app_code} {uuid} { authorization}"}
            
            if authorization.startswith('Bearer'):
                jwt_token = authorization[7:]
                decoded_jwt = JwtService().decode({ "token_type": "REFRESH" , "token": jwt_token})
                authorized = True
            
            return {
                "authorized": authorized,
                "app_name": app_name,
                "app_type": app_type,
                "app_version": app_version,
                "app_code": app_code,
                "client_ip": client_ip,
                "uuid": uuid,
                "decoded_jwt": decoded_jwt
            }
        except Exception as ex:
            fastapi_logger.error(f"Auth.validate_refresh: {str(ex)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    # app_info, app_account = self.init_auth(db)
    # decoded_jwt = app_info['decoded_jwt']
    def validate_service(self):
        app_key = self.request.headers.get("x-app-key")
        app_secret = self.request.headers.get("x-app-secret")

        if not app_key or not app_secret:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

        return {
            "app_key": app_key,
            "app_secret": app_secret
        }

    @staticmethod # decoded_jwt = Auth.validate_websocket
    def validate_websocket(authorization):
        if authorization.startswith('Bearer '):
            jwt_token = authorization[7:]
            decoded_jwt = JwtService().decode({"token":jwt_token})

        return decoded_jwt
        
    @staticmethod # Validate the email and return the details
    def validate_email(idToken):
        try:
            email_info = id_token.verify_oauth2_token(idToken, requests.Request())
            
            if not email_info:
                fastapi_logger.error(f"Error processing the Token ID")
                return HTTPException(status_code=400, detail="Invalid Request")
            
            return email_info
        
        except Exception as ex:
            fastapi_logger.error(f"Auth.validate_email: {str(ex)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")