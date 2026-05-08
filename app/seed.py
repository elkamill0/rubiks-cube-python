import json
from app.database import SessionLocal
from app.models.algorithms import Algorithm
from app.models.alg import Alg
from sqlalchemy import text

def seed():
    db = SessionLocal()
    db.query(Alg).delete()
    db.query(Algorithm).delete()
    db.execute(text("ALTER SEQUENCE algs_id_seq RESTART WITH 1"))
    db.execute(text("ALTER SEQUENCE algorithms_id_seq RESTART WITH 1"))


    files = [
        ("f2l1", "F2L_1"),
        ("f2l2", "F2L_2"),
        ("f2l3", "F2L_3"),
        ("f2l4", "F2L_4"),
        ("oll",  "OLL"),
        ("pll",  "PLL"),
    ]

    for filename, category in files:
        with open (f"cases_select/{filename}.json") as f:
            data = json.load(f)
        for item in data:
            algorithm = Algorithm(
                name=item["name"],
                img=item["img"],
                category=category,
            )
            db.add(algorithm)
            db.flush()


            for case in item["algs"]:
                alg = Alg(
                    algorithm_id=algorithm.id,
                    alg=case,
                )
                db.add(alg)

    for algorithm in db.query(Algorithm).all():
        first_alg = db.query(Alg).filter(Alg.algorithm_id == algorithm.id).first()
        if first_alg:
            first_alg.is_selected = True    

    db.commit()
    db.close()

    

if __name__ == "__main__":
    seed()