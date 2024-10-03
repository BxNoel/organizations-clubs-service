from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud,models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Organizations and Events API!"}

# Organization routes
@app.post("/organizations/", response_model=schemas.Organization)
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db=db, organization=organization)

@app.get("/organizations/", response_model=list[schemas.Organization])
def get_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations

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

# Event routes
@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)

@app.get("/events/", response_model=list[schemas.Event])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

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