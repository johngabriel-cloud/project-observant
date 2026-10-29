from app.database import SessionLocal
from app.models.models import Service
from app.crud.service import post_service

session = SessionLocal()

service = Service(
    service_name="Test Service", 
    url="http://example.com", 
    check_type="http", 
    interval=60
    )

post_service(session, service)
print(f"Service created: {service.service_id}, {service.service_name}, {service.url}, {service.check_type}, {service.interval}")
session.close()