from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import ExampleModel
from app.schemas import ExampleCreate, ExampleResponse

router = APIRouter(prefix="/examples", tags=["Examples"])


@router.get("/", response_model=list[ExampleResponse])
def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(ExampleModel).offset(skip).limit(limit).all()


@router.post("/", response_model=ExampleResponse)
def create_example(example: ExampleCreate, db: Session = Depends(get_db)):
    db_example = ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example
