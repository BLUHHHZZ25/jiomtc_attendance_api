from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, date, time
from typing import Optional


# ============================
# MEMBER SCHEMAS
# ============================
class MemberBase(BaseModel):
    name: str = Field(..., max_length=255)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=50)
    join_date: date
    status: str = Field(default='Active', max_length=20)
    address: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = Field(None, max_length=10)
    emergency_contact_name: Optional[str] = Field(None, max_length=255)
    emergency_contact_phone: Optional[str] = Field(None, max_length=50)
    notes: Optional[str] = None


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=50)
    join_date: Optional[date] = None
    status: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = Field(None, max_length=10)
    emergency_contact_name: Optional[str] = Field(None, max_length=255)
    emergency_contact_phone: Optional[str] = Field(None, max_length=50)
    notes: Optional[str] = None


class MemberResponse(MemberBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# USER SCHEMAS (Admin)
# ============================
class UserBase(BaseModel):
    username: str = Field(..., max_length=100)
    email: EmailStr
    full_name: str = Field(..., max_length=255)
    role: str = Field(default='Staff', max_length=20)
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=255)
    role: Optional[str] = Field(None, max_length=20)
    is_active: Optional[bool] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# SERVICE SCHEMAS
# ============================
class ServiceBase(BaseModel):
    service_name: str = Field(..., max_length=255)
    service_type: str = Field(..., max_length=50)
    description: Optional[str] = None
    default_day_of_week: Optional[str] = Field(None, max_length=10)
    default_time: Optional[time] = None
    is_active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    service_name: Optional[str] = Field(None, max_length=255)
    service_type: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None
    default_day_of_week: Optional[str] = Field(None, max_length=10)
    default_time: Optional[time] = None
    is_active: Optional[bool] = None


class ServiceResponse(ServiceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# ATTENDANCE SESSION SCHEMAS
# ============================
class AttendanceSessionBase(BaseModel):
    service_id: int
    session_date: date
    session_time: Optional[time] = None
    total_members_at_time: int
    total_present: int = 0
    total_absent: int = 0
    notes: Optional[str] = None
    recorded_by: Optional[int] = None


class AttendanceSessionCreate(AttendanceSessionBase):
    pass


class AttendanceSessionUpdate(BaseModel):
    service_id: Optional[int] = None
    session_date: Optional[date] = None
    session_time: Optional[time] = None
    total_members_at_time: Optional[int] = None
    total_present: Optional[int] = None
    total_absent: Optional[int] = None
    notes: Optional[str] = None
    recorded_by: Optional[int] = None


class AttendanceSessionResponse(AttendanceSessionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# ATTENDANCE RECORD SCHEMAS
# ============================
class AttendanceRecordBase(BaseModel):
    session_id: int
    member_id: int
    status: str = Field(..., max_length=20)
    check_in_time: Optional[time] = None
    notes: Optional[str] = None


class AttendanceRecordCreate(AttendanceRecordBase):
    pass


class AttendanceRecordUpdate(BaseModel):
    status: Optional[str] = Field(None, max_length=20)
    check_in_time: Optional[time] = None
    notes: Optional[str] = None


class AttendanceRecordResponse(AttendanceRecordBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# MEMBER GROUP SCHEMAS
# ============================
class MemberGroupBase(BaseModel):
    group_name: str = Field(..., max_length=255)
    description: Optional[str] = None
    leader_id: Optional[int] = None
    is_active: bool = True


class MemberGroupCreate(MemberGroupBase):
    pass


class MemberGroupUpdate(BaseModel):
    group_name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    leader_id: Optional[int] = None
    is_active: Optional[bool] = None


class MemberGroupResponse(MemberGroupBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ============================
# MEMBER GROUP ASSIGNMENT SCHEMAS
# ============================
class MemberGroupAssignmentBase(BaseModel):
    member_id: int
    group_id: int
    joined_date: date
    role: Optional[str] = Field(None, max_length=100)
    is_active: bool = True


class MemberGroupAssignmentCreate(MemberGroupAssignmentBase):
    pass


class MemberGroupAssignmentUpdate(BaseModel):
    joined_date: Optional[date] = None
    role: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = None


class MemberGroupAssignmentResponse(MemberGroupAssignmentBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
        
# ============================
# LOGIN USER SCHEMA
# ============================

class LoginUserBase(BaseModel):
    email: EmailStr | None = None 
    password: str | None = Field(None, min_length=6) 
    idToken: str | None  = Field(None, min_length=6) 


# class UserCreate(UserBase):
#     password: str


# class UserUpdate(BaseModel):
#     username: Optional[str] = Field(None, max_length=100)
#     email: Optional[EmailStr] = None
#     full_name: Optional[str] = Field(None, max_length=255)
#     role: Optional[str] = Field(None, max_length=20)
#     is_active: Optional[bool] = None
#     password: Optional[str] = None


# class UserResponse(UserBase):
#     id: int
#     last_login: Optional[datetime] = None
#     created_at: datetime
#     updated_at: Optional[datetime] = None
    
#     class Config:
#         from_attributes = True