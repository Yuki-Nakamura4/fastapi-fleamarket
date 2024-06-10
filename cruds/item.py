from enum import Enum
from sqlalchemy.orm import Session
from schemas import ItemCreate
from models import Item

def find_all(db: Session):
    return db.query(Item).all()

def find_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()

def find_by_name(db:Session, name: str):
    return db.query(Item).filter(Item.name.like(f"%{name}%")).all()

def create(db: Session, item_create: ItemCreate):
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item)
    db.commit()
    return new_item

def update(db: Session, id:int, item_update):
    item = find_by_id(db, id)
    if item is None:
        return None
    item.name = item.name if item_update.name is None else item_update.name
    item.price = item.price if item_update.price is None else item_update.price
    item.description = item.description if item_update.description is None else item_update.description
    item.status = item.status if item_update.status is None else item_update.status
    db.add(item)
    db.commit()

    return item

def delete(db: Session, id:int):
    item = find_by_id(db, id)
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item