from pydantic import BaseModel


class Solution(BaseModel):
    moves: list[str]
    total_moves: int


class ScrambleResponse(BaseModel):
    scramble: str
    cube_state: str


class ScrambleRequest(BaseModel):
    scramble: str | None = None
    color: str = "y"


class SolveResponse(BaseModel):
    solutions: list[Solution]


class SolveRequest(BaseModel):
    scramble: str | None = None
    cross_color: str = "y"
    cross_length: int = 6
