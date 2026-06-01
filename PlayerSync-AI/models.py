from sqlalchemy import Column, Integer, Float
from database import Base

class PlayerPrediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    feature_1 = Column(Float, nullable=False)
    feature_2 = Column(Float, nullable=False)
    feature_3 = Column(Float, nullable=False)
    feature_4 = Column(Float, nullable=False)  # Added 4th feature
    assigned_cluster = Column(Integer, nullable=False)