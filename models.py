# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class DetectionResult(Base):
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Float)
    x_min = Column(Integer)
    y_min = Column(Integer)
    x_max = Column(Integer)
    y_max = Column(Integer)