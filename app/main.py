from fastapi import FastAPI

from app.routers.algorithm import router as algorithm_router
from app.routers.cube import router

app = FastAPI()
app.include_router(router)
app.include_router(algorithm_router)


@app.get("/health")
def health():
    return {"status": "ok"}
