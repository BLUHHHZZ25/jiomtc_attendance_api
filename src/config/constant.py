from enum import Enum

class Status(Enum):
    PROGRESS = 'PROGRESS'
    SUCCESSFUL = 'SUCCESSFUL'
    FAILED = 'FAILED'

class AccountStatus(Enum):
    INITIAL = 'INITIAL'
    FOR_OTP = 'FOR_OTP'
    VERIFIED = 'VERIFIED'
    NEW = 'NEW'
    REGISTERED = 'REGISTERED'

class AuthValidation(Enum):
    LOGGED_IN = 'LOGGED_IN'
    ACCESS_TOKEN = 'ACCESS_TOKEN'
    REFRESH_TOKEN = 'REFRESH_TOKEN'
    

class AccountSigninAction(Enum):
    PWD = "pwd"
    OTP = "otp"
    EMAIL = "email"
    MPIN = "mpin"

class MFAStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETE = "delete"
    
class DeliveryOptions(Enum):
    REGULAR = 'REGULAR'
    PRIORITY = 'PRIORITY'
    POOLING = 'POOLING'
