from fastapi import FastAPI, Query, HTTPException, Depends, status, Response, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from math import ceil
from uuid import uuid4
import asyncio
from typing import Optional  # Added for optional query parameters

from . import crud, models, schemas
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# In-memory storage for task statuses
task_storage = {}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Organizations and Events API!"}

# ----------------------------
# Organization Endpoints
# ----------------------------

@app.post("/organizations/", response_model=schemas.OrganizationCreateResponse)
def create_organization(
    organization: schemas.OrganizationCreate,
    db: Session = Depends(get_db),
    background_tasks: BackgroundTasks = None,
    is_async: bool = Query(False, description="Set to true for asynchronous creation"),
    response: Response = Response()
):
    try:
        if is_async:
            task_id = str(uuid4())
            background_tasks.add_task(process_organization_creation, db, organization, task_id)
            status_url = f"/organizations/status/{task_id}"
            response.status_code = status.HTTP_202_ACCEPTED
            return schemas.OrganizationCreateResponse(task_id=task_id, status="Processing", status_url=status_url)
        else:
            new_organization = crud.create_organization(db=db, organization=organization)
            location = f"/organizations/{new_organization.id}"
            response.headers["Location"] = location
            response.headers["Link"] = f'<{location}>; rel="self"'
            response.status_code = status.HTTP_201_CREATED
            return schemas.OrganizationCreateResponse(id=new_organization.id, status="Created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_organization_creation(db: Session, organization: schemas.OrganizationCreate, task_id: str):
    try:
        # Simulate a time-consuming process (e.g., complex validations or external API calls)
        await asyncio.sleep(10)  # Simulating a long-running task
        new_organization = crud.create_organization(db=db, organization=organization)
        task_storage[task_id] = {"status": "Completed", "organization_id": new_organization.id}
    except Exception as e:
        task_storage[task_id] = {"status": "Failed", "error": str(e)}

@app.get("/organizations/status/{task_id}", response_model=schemas.OrganizationStatusResponse)
def get_organization_status(task_id: str):
    task_info = task_storage.get(task_id)
    if not task_info:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_info

@app.get("/organizations/", response_model=schemas.PaginatedOrganizationResponse)
def get_organizations(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page"),
    name: Optional[str] = Query(None, description="Filter by organization name"),
    category: Optional[str] = Query(None, description="Filter by organization category")
):
    skip = (page - 1) * size
    filters = {}
    if name:
        filters['name'] = name
    if category:
        filters['category'] = category
    organizations = crud.get_organizations(db, filters=filters, skip=skip, limit=size)
    total = db.query(func.count(models.Organization.id)).scalar()
    pages = ceil(total / size)
    if page > pages and total > 0:
        raise HTTPException(status_code=404, detail="Page not found")
    return {
        "items": organizations,
        "total": total,
        "page": page,
        "size": size,
        "pages": pages
    }

@app.get("/organizations/{organization_id}/", response_model=schemas.Organization)
def get_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organization = crud.get_organization(db, organization_id=organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@app.put("/organizations/{organization_id}/", response_model=schemas.Organization)
def update_organization(organization_id: int, organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_organization = crud.update_organization(db, organization_id=organization_id, organization=organization)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@app.delete("/organizations/{organization_id}/", response_model=schemas.Organization)
def delete_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organization = crud.delete_organization(db, organization_id=organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

# ----------------------------
# Event Endpoints
# ----------------------------

@app.post("/events/", response_model=schemas.EventCreateResponse)
def create_event(
    event: schemas.EventCreate,
    background_tasks: BackgroundTasks,
    response: Response,
    db: Session = Depends(get_db),
    is_async: bool = Query(False, description="Set to true for asynchronous creation")
):
    try:
        if is_async:
            task_id = str(uuid4())
            background_tasks.add_task(process_event_creation, db, event, task_id)
            status_url = f"/events/status/{task_id}"
            response.status_code = status.HTTP_202_ACCEPTED
            return schemas.EventCreateResponse(task_id=task_id, status="Processing", status_url=status_url)
        else:
            new_event = crud.create_event(db=db, event=event)
            event_url = f"/events/{new_event.id}"
            response.headers["Location"] = event_url
            response.headers["Link"] = f'<{event_url}>; rel="self"'
            response.status_code = status.HTTP_201_CREATED
            return schemas.EventCreateResponse(id=new_event.id, status="Created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_event_creation(db: Session, event: schemas.EventCreate, task_id: str):
    try:
        await asyncio.sleep(10)
        new_event = crud.create_event(db=db, event=event)
        task_storage[task_id] = {"status": "Completed", "event_id": new_event.id}
    except Exception as e:
        task_storage[task_id] = {"status": "Failed", "error": str(e)}

@app.get("/events/status/{task_id}", response_model=schemas.EventStatusResponse)
def get_event_status(task_id: str):
    task_info = task_storage.get(task_id)
    if not task_info:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_info

@app.get("/events/", response_model=schemas.PaginatedEventResponse)
def get_events(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page"),
    name: Optional[str] = Query(None, description="Filter by event name"),
    date: Optional[str] = Query(None, description="Filter by event date")
):
    skip = (page - 1) * size
    filters = {}
    if name:
        filters['name'] = name
    if date:
        filters['date'] = date
    events = crud.get_events(db, filters=filters, skip=skip, limit=size)
    total = db.query(func.count(models.Event.id)).scalar()
    pages = ceil(total / size)
    if page > pages and total > 0:
        raise HTTPException(status_code=404, detail="Page not found")
    return {
        "items": events,
        "total": total,
        "page": page,
        "size": size,
        "pages": pages
    }

@app.get("/events/{event_id}/", response_model=schemas.Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@app.put("/events/{event_id}/", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = crud.update_event(db, event_id=event_id, event=event)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@app.delete("/events/{event_id}/", response_model=schemas.Event)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.delete_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
