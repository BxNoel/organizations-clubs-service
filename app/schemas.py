from pydantic import BaseModel
from typing import List, Optional

# Organization Pydantic Models
class OrganizationBase(BaseModel):
    organization_name: str
    created_at: Optional[str] = None  # Use datetime type if preferred
    organization_code: Optional[str] = None
    category: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    organization_id: int

    class Config:
        orm_mode = True


# Event Pydantic Models
class EventBase(BaseModel):
    event_name: str
    created_at: Optional[str] = None  # Use datetime type if preferred
    event_code: Optional[str] = None
    start_time: Optional[str] = None  # Use datetime type if preferred
    end_time: Optional[str] = None
    date: Optional[str] = None  # Use datetime type if preferred
    location: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    event_id: int

    class Config:
        orm_mode = True
