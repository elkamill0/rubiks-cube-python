from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.dependencies import get_db
from app.models.alg import Alg
from app.models.algorithms import Algorithm
from app.schemas.algorithm import AlgorithmResponse, AlgUpdate

router = APIRouter(prefix="/algorithms", tags=["algorithms"])


@router.get("/", response_model=list[AlgorithmResponse])
def get_algorithms(category: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Algorithm).options(joinedload(Algorithm.algs))
    if category:
        query = query.filter(Algorithm.category == category)
    return query.all()


@router.patch("/algs/{alg_id}")
def update_alg(alg_id: int, body: AlgUpdate, db: Session = Depends(get_db)):
    alg = db.query(Alg).filter(Alg.id == alg_id).first()

    if not alg:
        raise HTTPException(status_code=404, detail="Alg not found")

    if body.is_selected:
        db.query(Alg).filter(Alg.algorithm_id == alg.algorithm_id).update(
            {"is_selected": False}
        )

    alg.is_selected = body.is_selected
    db.commit()
    db.refresh(alg)
    return alg


if __name__ == "__main__":
    get_algorithms()
