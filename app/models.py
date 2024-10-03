from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from .database import Base

class Organization(Base):
    __tablename__ = "organization_database"
    
    organization_id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(Text, nullable=True)
    created_at = Column(Text, nullable=True)  # Use appropriate type for timestamp if needed
    organization_code = Column(Text, nullable=True)
    category = Column(Text, nullable=True)


class Event(Base):
    __tablename__ = "events_database"
    
    event_id = Column(Integer, primary_key=True, index=True)
    event_name = Column(Text, nullable=True)
    created_at = Column(Text, nullable=True)  # Use appropriate type for timestamp if needed
    event_code = Column(Text, nullable=True)
    start_time = Column(Text, nullable=True)  # Use Time or DateTime if you want to represent specific times
    end_time = Column(Text, nullable=True)
    date = Column(Date, nullable=True)
    location = Column(Text, nullable=True)
