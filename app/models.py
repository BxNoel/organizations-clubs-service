from sqlalchemy import Column, BigInteger, String, Text, DateTime, Time, Date
from sqlalchemy.sql import func
from .database import Base

class Organization(Base):
    __tablename__ = "organization_database"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    name = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    code = Column(String(50))
    category = Column(String(100)) 

class Event(Base):
    __tablename__ = "events_database"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    name = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    code = Column(String(50)) 
    start_time = Column(Time)
    end_time = Column(Time)
    date = Column(Date)
    location = Column(Text)
    