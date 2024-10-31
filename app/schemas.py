from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date, time

class OrganizationBase(BaseModel):
    name: str
    code: Optional[str] = None
    category: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PaginatedOrganizationResponse(BaseModel):
    items: List[Organization]
    total: int
    page: int
    size: int
    pages: int

class EventBase(BaseModel):
    name: str
    code: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    date: Optional[datetime] = None
    location: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PaginatedEventResponse(BaseModel):
    items: List[Event]
    total: int
    page: int
    size: int
    pages: int


class OrganizationCreateResponse(BaseModel):
    id: Optional[int] = None 
    task_id: Optional[str] = None 
    status: str
    status_url: Optional[str] = None

class OrganizationStatusResponse(BaseModel):
    status: str
    organization_id: Optional[int] = None 
    error: Optional[str] = None  

class EventCreateResponse(BaseModel):
    id: Optional[int] = None 
    task_id: Optional[str] = None 
    status: str
    status_url: Optional[str] = None  

class EventStatusResponse(BaseModel):
    status: str
    event_id: Optional[int] = None
    error: Optional[str] = None



class LinkHeader(BaseModel):
    url: str
    rel: str