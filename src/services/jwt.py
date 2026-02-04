import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
import json
import time

from config_setting import setting
from config.log import logger as fastapi_logger


class JwtService:
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24   # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 10 # 10 days | forever login
    ALGORITHM = "HS256"

    def encode(self, params, payload):
        try:
            key = setting.JWT_SECRET_KEY
            expires_in = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

            if "token_type" in params:
                if params['token_type'] == "SIGNUP":
                    key = setting.JWT_SIGNUP_KEY
                elif params['token_type'] == "REFRESH":
                    key = setting.JWT_REFRESH_SECRET_KEY
                    expires_in = datetime.utcnow() + timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
            
            payload['exp'] = expires_in
            payload['sub'] = setting.SUB_NAME
            to_encode = payload
            encoded_jwt = jwt.encode(to_encode, key, self.ALGORITHM)

            return encoded_jwt
        except Exception as ex:
            fastapi_logger.error(f"JwtService.encode is failed: {str(ex)}")
            raise Exception(f"JWT Authentication Error: {str(ex)}")

    def decode(self, params):
        try:
            key = setting.JWT_SECRET_KEY

            if "token_type" in params:
                if params['token_type'] == "SIGNUP":
                    key = setting.JWT_SIGNUP_KEY
                elif params['token_type'] == "REFRESH":
                    key = setting.JWT_REFRESH_SECRET_KEY
            
            decoded_jwt = jwt.decode(params['token'], key, self.ALGORITHM)
            return decoded_jwt
        except Exception as ex:
            fastapi_logger.error(f"JwtService.decode is failed: {str(ex)}")
            raise Exception(f"JWT Authentication Error: {str(ex)}")


