# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import DetectionResult, DetectionResultCreate
from crud import get_detection_result, get_detection_results, create_detection_result

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints
@app.post("/detection_results/", response_model=DetectionResult)
def create_result(result: DetectionResultCreate, db: Session = Depends(get_db)):
    return create_detection_result(db, result)

@app.get("/detection_results/", response_model=list[DetectionResult])
def read_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = get_detection_results(db, skip=skip, limit=limit)
    return results

@app.get("/detection_results/{result_id}", response_model=DetectionResult)
def read_result(result_id: int, db: Session = Depends(get_db)):
    result = get_detection_result(db, result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return result