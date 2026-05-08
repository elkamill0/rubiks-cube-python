from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Algorithm(Base):
    __tablename__ = "algorithms"
    algs = relationship("Alg", back_populates="algorithm")
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    img = Column(String)
