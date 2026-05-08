from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.alg import Alg


class Algorithm(Base):
    __tablename__ = "algorithms"
    algs = relationship("Alg", back_populates="algorithm")
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    img = Column(String)
