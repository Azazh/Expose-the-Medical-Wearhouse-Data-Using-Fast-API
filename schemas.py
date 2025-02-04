# schemas.py
from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_path: str
    class_label: str
    confidence: float
    x_min: int
    y_min: int
    x_max: int
    y_max: int

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True