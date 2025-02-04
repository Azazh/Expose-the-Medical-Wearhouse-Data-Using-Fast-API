# crud.py
from sqlalchemy.orm import Session
from models import DetectionResult
from schemas import DetectionResultCreate

def get_detection_result(db: Session, result_id: int):
    return db.query(DetectionResult).filter(DetectionResult.id == result_id).first()

def get_detection_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DetectionResult).offset(skip).limit(limit).all()

def create_detection_result(db: Session, result: DetectionResultCreate):
    db_result = DetectionResult(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result