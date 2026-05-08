from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Alg(Base):
    __tablename__ = "algs"
    algorithm = relationship("Algorithm", back_populates="algs")
    id = Column(Integer, primary_key=True)
    algorithm_id = Column(Integer, ForeignKey("algorithms.id"))
    alg = Column(String)
    is_selected = Column(Boolean, default=False)
