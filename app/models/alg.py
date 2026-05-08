from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Alg(Base):

    __tablename__ = "algs"
    algorithm = relationship("Algorithm", back_populates="algs")
    id = Column(Integer, primary_key=True)
    algorithm_id = Column(Integer, ForeignKey("algorithms.id"))
    alg = Column(String)
    is_selected = Column(Boolean, default=False)
