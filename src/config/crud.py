from config import models
from config.log import logger as fastapi_logger
from utils.auth import Auth
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
                username=params['username'],
                email=params['email'],
                password_hash=params['password'],
                full_name=params['full_name'],
                role=params['role']
            )
            fastapi_logger.info(f" params password {params['password']} -- type {(type(params['password']))}")
            db.add(create_user)
            db.commit()
            db.refresh(create_user)
            
            return create_user
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
        
class Member:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_EMAIL':
                    return db.query(models.Member).filter(models.Member.email == params['email']).first()
                elif action == 'BY_ID':
                    return db.query(models.Member).filter(models.Member.id == params['id']).first()
                elif action == 'BY_ALL':
                    return db.query(models.Member).all()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"Member.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_member = models.Member(
                name=params['name'],
                email=params['email'],
                phone=params['phone'],
                join_date=params['join_date'],
                status=params['status'],
                address=params['address'],
                date_of_birth=params['date_of_birth'],
                gender=params['gender'],
                emergency_contact_name=params['emergency_contact_name'],
                emergency_contact_phone=params['emergency_contact_phone'],
                notes=params['notes'],
            )

            db.add(create_member)
            db.commit()
            db.refresh(create_member)
            
            return create_member
        except Exception as ex:
            fastapi_logger.error(f"Member.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            member_data = db.query(models.Member).filter(models.Member.email == params['email']).first()

            if not member_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_PROFILE":
                    member_data.name=params['name'],
                    # member_data.email=params['email'],
                    member_data.phone=params['phone'],
                    member_data.join_date=params['join_date'],
                    member_data.status=params['status'],
                    member_data.address=params['address'],
                    member_data.date_of_birth=params['date_of_birth'],
                    member_data.gender=params['gender'],
                    member_data.emergency_contact_name=params['emergency_contact_name'],
                    member_data.emergency_contact_phone=params['emergency_contact_phone'],
                    member_data.notes=params['notes'],

                
            db.add(member_data)
            db.commit()
            db.refresh(member_data)
            return member_data
        except Exception as ex:
            fastapi_logger.error(f"Member.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

        
class Services:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_SERVICE_NAME':
                    return db.query(models.Service).filter(models.Service.service_name == params['service_name']).first()
                elif action == 'BY_ID':
                    return db.query(models.Service).filter(models.Service.id == params['id']).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"Service.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_services = models.Service(
                service_name=params['service_name'],
                service_type=params['service_type'],
                description=params['description'],
                default_day_of_week=params['default_day_of_week'],
                default_time=params['default_time'],
                is_active=params['is_active']
            )

            db.add(create_services)
            db.commit()
            db.refresh(create_services)
            
            return create_services
        except Exception as ex:
            fastapi_logger.error(f"Service.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            services_data = db.query(models.Service).filter(models.Service.id == params['id']).first()

            if not services_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_SERVICES":
                    services_data.service_name=params['service_name'],
                    services_data.service_type=params['service_type'],
                    services_data.description=params['description'],
                    services_data.default_day_of_week=params['default_day_of_week'],
                    services_data.default_time=params['default_time'],
                    services_data.is_active=params['is_active']

                
            db.add(services_data)
            db.commit()
            db.refresh(services_data)
            return services_data
        except Exception as ex:
            fastapi_logger.error(f"Service.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")
        
class MemberGroup:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_GROUP_NAME':
                    return db.query(models.MemberGroup).filter(models.MemberGroup.group_name == params['group_name']).first()
                elif action == 'BY_ID':
                    return db.query(models.MemberGroup).filter(models.MemberGroup.id == params['id']).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"MemberGroup.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_services = models.MemberGroup(
                group_name=params['group_name'],
                description=params['description'],
                leader_id=params['leader_id'],
                is_active=params['is_active']
            )

            db.add(create_services)
            db.commit()
            db.refresh(create_services)
            
            return create_services
        except Exception as ex:
            fastapi_logger.error(f"MemberGroup.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            memebergroup_data = db.query(models.MemberGroup).filter(models.MemberGroup.id == params['id']).first()

            if not memebergroup_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_MEMBER_GROUP":
                    memebergroup_data.group_name=params['group_name'],
                    memebergroup_data.description=params['description'],
                    memebergroup_data.leader_id=params['leader_id'],
                    memebergroup_data.is_active=params['is_active']

                
            db.add(memebergroup_data)
            db.commit()
            db.refresh(memebergroup_data)
            return memebergroup_data
        except Exception as ex:
            fastapi_logger.error(f"MemberGroup.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

        
class MemberGroupAssignment:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_ID':
                    return db.query(models.MemberGroupAssignment).filter(models.MemberGroupAssignment.id == params['id']).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"MemberGroupAssignment.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_member_assignment = models.MemberGroupAssignment(
                member_id=params['member_id'],
                group_id=params['group_id'],
                joined_date=params['joined_date'],
                role=params['role'],
                is_active=params['is_active']
            )

            db.add(create_member_assignment)
            db.commit()
            db.refresh(create_member_assignment)
            
            return create_member_assignment
        except Exception as ex:
            fastapi_logger.error(f"MemberGroupAssignment.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            memeber_assignment_data = db.query(models.MemberGroupAssignment).filter(models.MemberGroupAssignment.id == params['id']).first()

            if not memeber_assignment_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_ASSIGNMENT_GROUP":              
                    memeber_assignment_data.member_id=params['member_id'],
                    memeber_assignment_data.group_id=params['group_id'],
                    memeber_assignment_data.joined_date=params['joined_date'],
                    memeber_assignment_data.role=params['role'],
                    memeber_assignment_data.is_active=params['is_active']

                
            db.add(memeber_assignment_data)
            db.commit()
            db.refresh(memeber_assignment_data)
            return memeber_assignment_data
        except Exception as ex:
            fastapi_logger.error(f"MemberGroupAssignment.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

        
class AttendanceSession:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_ID':
                    return db.query(models.AttendanceSession).filter(models.AttendanceSession.id == params['id']).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"AttendanceSession.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            create_attendance_session = models.AttendanceSession(
                service_id=params['service_id'],
                session_date=params['session_date'],
                session_time=params['session_time'],
                total_members_at_time=params['total_members_at_time'],
                total_present=params['total_present'],
                total_absent=params['total_absent'],
                notes=params['notes'],
                recorded_by=params['recorded_by'],
            )

            db.add(create_attendance_session)
            db.commit()
            db.refresh(create_attendance_session)
            
            return create_attendance_session
        except Exception as ex:
            fastapi_logger.error(f"AttendanceSession.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            session_data = db.query(models.AttendanceSession).filter(models.AttendanceSession.id == params['id']).first()

            if not session_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_ATTENDANCE_SESSION":                                  
                    session_data.service_id=params['service_id'],
                    session_data.session_date=params['session_date'],
                    session_data.session_time=params['session_time'],
                    session_data.total_members_at_time=params['total_members_at_time'],
                    session_data.total_present=params['total_present'],
                    session_data.total_absent=params['total_absent'],
                    session_data.notes=params['notes'],
                    session_data.recorded_by=params['recorded_by'],

                
            db.add(session_data)
            db.commit()
            db.refresh(session_data)
            return session_data
        except Exception as ex:
            fastapi_logger.error(f"AttendanceSession.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")


class AttendanceRecord:
    
    @staticmethod
    def get(db, params):
        try:
            if 'action_type' in params:
                action = params['action_type']
                if action == 'BY_ID':
                    return db.query(models.AttendanceRecord).filter(models.AttendanceRecord.id == params['id']).first()
                return {"No Type Found"}
        except Exception as ex:
            fastapi_logger.error(f"AttendanceRecord.get is failed: {str(ex)} - action_type: {params['action_type']}")
            raise Exception(f"DB Error: {str(ex)}")
        
    def create(db, params):
        try:
            attendance_record = models.AttendanceRecord(
                session_id=params['session_id'],
                memeber_id=params['memeber_id'],
                status=params['status'],
                check_in_time=params['check_in_time'],
                notes=params['notes']
            )

            db.add(attendance_record)
            db.commit()
            db.refresh(attendance_record)
            
            return attendance_record
        except Exception as ex:
            fastapi_logger.error(f"AttendanceRecord.create is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

            
    def update(db, params):
        try:
            attendance_data = db.query(models.AttendanceRecord).filter(models.AttendanceRecord.id == params['id']).first()

            if not attendance_data:
                raise Exception(f"Account not found")

            if 'action_type' in params:
                action = params['action_type']
                if action == "UPDATE_RECORD":                                  
                    attendance_data.session_id=params['session_id'],
                    attendance_data.memeber_id=params['memeber_id'],
                    attendance_data.status=params['status'],
                    attendance_data.check_in_time=params['check_in_time'],
                    attendance_data.notes=params['notes']

                
            db.add(attendance_data)
            db.commit()
            db.refresh(attendance_data)
            return attendance_data
        except Exception as ex:
            fastapi_logger.error(f"AttendanceRecord.update is failed: {str(ex)}")
            raise Exception(f"DB Error: {str(ex)}")

        