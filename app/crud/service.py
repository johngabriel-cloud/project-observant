from app.models.models import Service
from sqlalchemy import select


def post_service(session, service):
    try:
        session.add(service)
        session.commit()
    except:
        session.rollback()
        raise
    return service

def get_service(session, service_id):
    statement = select(Service).where(Service.service_id == service_id)
    result = session.execute(statement)
    service = result.scalar_one_or_none()
    return service

def update_service(session, service_id, new_url, new_interval, new_check_type):
    try:
        statement = select(Service).where(Service.service_id == service_id)
        result = session.execute(statement)
        service = result.scalar_one_or_none()
        if service is None:
            return None
        service.url = new_url
        service.interval = new_interval
        service.check_type = new_check_type
        session.commit()
    except:
        session.rollback()
        raise
    return service

def delete_service(session, service_id):
    try:
        statement = select(Service).where(Service.service_id == service_id)
        result = session.execute(statement)
        service = result.scalar_one_or_none()
        if service is None:
            return None
        session.delete(service)
        session.commit()
    except:
        session.rollback()
        raise
    return service