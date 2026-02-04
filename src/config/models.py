from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Date, Time, Text, 
    ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Member(Base):
    """Members table - stores information about church/organization members"""
    __tablename__ = "members"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(50))
    join_date = Column(Date, nullable=False, index=True)
    status = Column(String(20), default='Active', index=True)
    address = Column(Text)
    date_of_birth = Column(Date)
    gender = Column(String(10))
    emergency_contact_name = Column(String(255))
    emergency_contact_phone = Column(String(50))
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    attendance_records = relationship("AttendanceRecord", back_populates="member", cascade="all, delete-orphan")
    group_assignments = relationship("MemberGroupAssignment", back_populates="member", cascade="all, delete-orphan")
    led_groups = relationship("MemberGroup", back_populates="leader", foreign_keys="MemberGroup.leader_id")


class User(Base):
    """Users table - stores admin/staff accounts for the system"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(String(20), default='Staff', index=True)
    is_active = Column(Boolean, default=True, index=True)
    last_login = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    recorded_sessions = relationship("AttendanceSession", back_populates="recorder")


class Service(Base):
    """Services table - stores different types of services/events"""
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(255), nullable=False)
    service_type = Column(String(50), nullable=False, index=True)
    description = Column(Text)
    default_day_of_week = Column(String(10))
    default_time = Column(Time)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    attendance_sessions = relationship("AttendanceSession", back_populates="service", cascade="all, delete-orphan")


class AttendanceSession(Base):
    """Attendance sessions table - stores individual attendance sessions"""
    __tablename__ = "attendance_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey('services.id', ondelete='CASCADE'), nullable=False, index=True)
    session_date = Column(Date, nullable=False, index=True)
    session_time = Column(Time)
    total_members_at_time = Column(Integer, nullable=False)
    total_present = Column(Integer, default=0)
    total_absent = Column(Integer, default=0)
    notes = Column(Text)
    recorded_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    __table_args__ = (
        UniqueConstraint('service_id', 'session_date', name='uq_service_session_date'),
    )
    
    # Relationships
    service = relationship("Service", back_populates="attendance_sessions")
    recorder = relationship("User", back_populates="recorded_sessions")
    attendance_records = relationship("AttendanceRecord", back_populates="session", cascade="all, delete-orphan")


class AttendanceRecord(Base):
    """Attendance records table - stores individual member attendance records"""
    __tablename__ = "attendance_records"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('attendance_sessions.id', ondelete='CASCADE'), nullable=False, index=True)
    member_id = Column(Integer, ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    status = Column(String(20), nullable=False, index=True)
    check_in_time = Column(Time)
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    __table_args__ = (
        UniqueConstraint('session_id', 'member_id', name='uq_session_member'),
    )
    
    # Relationships
    session = relationship("AttendanceSession", back_populates="attendance_records")
    member = relationship("Member", back_populates="attendance_records")


class MemberGroup(Base):
    """Member groups table - stores groups/small groups/ministries"""
    __tablename__ = "member_groups"
    
    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String(255), nullable=False)
    description = Column(Text)
    leader_id = Column(Integer, ForeignKey('members.id'), index=True)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    leader = relationship("Member", back_populates="led_groups", foreign_keys=[leader_id])
    member_assignments = relationship("MemberGroupAssignment", back_populates="group", cascade="all, delete-orphan")


class MemberGroupAssignment(Base):
    """Member group assignments table - maps members to groups"""
    __tablename__ = "member_group_assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    group_id = Column(Integer, ForeignKey('member_groups.id', ondelete='CASCADE'), nullable=False, index=True)
    joined_date = Column(Date, nullable=False)
    role = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('member_id', 'group_id', name='uq_member_group'),
    )
    
    # Relationships
    member = relationship("Member", back_populates="group_assignments")
    group = relationship("MemberGroup", back_populates="member_assignments")