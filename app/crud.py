from sqlalchemy.orm import Session
from . import models, schemas

# Organization functions
def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()

def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organization).offset(skip).limit(limit).all()

def create_organization(db: Session, organization: schemas.OrganizationCreate):
    print(organization)
    db_organization = models.Organization(**organization.model_dump())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def update_organization(db: Session, organization_id: int, organization: schemas.OrganizationCreate):
    db_organization = db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    if db_organization:
        for key, value in organization.dict().items():
            setattr(db_organization, key, value)
        db.commit()
        db.refresh(db_organization)
    return db_organization

def delete_organization(db: Session, organization_id: int):
    db_organization = db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    if db_organization:
        db.delete(db_organization)
        db.commit()
    return db_organization

# Event functions
def get_event(db: Session, event_id: int):
    # print(db.query(models.Event).filter(models.Event.id == event_id).first())
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, event_id: int, event: schemas.EventCreate):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        for key, value in event.dict().items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
