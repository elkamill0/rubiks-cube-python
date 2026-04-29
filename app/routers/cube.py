from fastapi import APIRouter
from app.schemas.cube import ScrambleRequest, ScrambleResponse, SolveRequest, SolveResponse
from app.services.cube_service import get_scramble, solve_cube

router = APIRouter(prefix="/cube", tags=["cube"])

@router.post("/scramble", response_model=ScrambleResponse)
def scramble(request: ScrambleRequest):
    scramble, state = get_scramble(request.scramble, request.color)
    return ScrambleResponse(scramble=scramble, cube_state=state)

@router.post("/solve", response_model=SolveResponse)
def solve(request: SolveRequest):
    return SolveResponse(solutions=solve_cube(request.scramble, request.cross_color, request.cross_length))
