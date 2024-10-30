from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from .database import Base

class Organization(Base):
    __tablename__ = "organization_database"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=True)
    created_at = Column(Text, nullable=True)  # Use appropriate type for timestamp if needed
    code = Column(Text, nullable=True)
    category = Column(Text, nullable=True)


class Event(Base):
    __tablename__ = "events_database"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=True)
    created_at = Column(Text, nullable=True)  # Use appropriate type for timestamp if needed
    code = Column(Text, nullable=True)
    start_time = Column(Text, nullable=True)  # Use Time or DateTime if you want to represent specific times
    end_time = Column(Text, nullable=True)
    date = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
