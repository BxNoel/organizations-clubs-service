from pydantic import BaseModel
from typing import List, Optional

# Organization Pydantic Models
class OrganizationBase(BaseModel):
    id: int
    name: str
    created_at: Optional[str] = None
    code: Optional[str] = None
    category: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int

    class Config:
        orm_mode = True


# Event Pydantic Models
class EventBase(BaseModel):
    id: int
    name: str
    created_at: Optional[str] = None  # Use datetime type if preferred
    code: Optional[str] = None
    start_time: Optional[str] = None  # Use datetime type if preferred
    end_time: Optional[str] = None
    date: Optional[str] = None  # Use datetime type if preferred
    location: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
