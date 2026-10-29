from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

#base class for the models
class Base(DeclarativeBase):
    pass

#models for the database tables
class Service(Base):
    __tablename__ = "services"

    service_id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str] = mapped_column(unique=True)
    url: Mapped[str]
    check_type: Mapped[str]
    interval: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    #relationships to other tables
    #back_populates is used to specify the relationship in the other table
    #cascade is used when deleting a service, also delete the related check results and monitoring events
    check_results: Mapped[list["CheckResult"]] = relationship("CheckResult", back_populates="service", cascade="all, delete-orphan")
    monitoring_events: Mapped[list["MonitoringEvent"]] = relationship("MonitoringEvent", back_populates="service", cascade="all, delete-orphan")

class CheckResult(Base):
    __tablename__ = "check_results"

    check_result_id: Mapped[int] = mapped_column(primary_key=True)
    #ondelete="CASCADE" is used to delete the check results when the service is deleted
    service_id: Mapped[int] = mapped_column(ForeignKey("services.service_id", ondelete="CASCADE"))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    response_type: Mapped[str]
    result: Mapped[str]
    response_time: Mapped[int]

    service: Mapped["Service"] = relationship("Service", back_populates="check_results")

class MonitoringEvent(Base):
    __tablename__ = "monitoring_events"

    monitoring_event_id: Mapped[int] = mapped_column(primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.service_id", ondelete="CASCADE"))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    event_type: Mapped[str]

    service: Mapped["Service"] = relationship("Service", back_populates="monitoring_events")

class SystemEvent(Base):
    __tablename__ = "system_events"

    system_event_id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    event_type: Mapped[str]