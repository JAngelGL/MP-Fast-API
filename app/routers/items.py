from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/items", tags=["Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}