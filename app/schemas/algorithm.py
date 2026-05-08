from pydantic import BaseModel


class AlgResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    alg: str
    is_selected: bool


class AlgorithmResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    category: str
    name: str
    img: str
    algs: list[AlgResponse]


class AlgorithmRequest(BaseModel):
    scramble: str | None = None
    color: str = "y"


class AlgUpdate(BaseModel):
    is_selected: bool
