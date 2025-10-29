import streamlit as st
from cube import Cube
from scramble import generate_scramble
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL


# Inicjalizacja kostki w sesji
if "cube" not in st.session_state:
    st.session_state.cube = Cube()

cube = st.session_state.cube

display = st.empty()  # miejsce do wyświetlania kostki

# Lista ruchów
# move_names = [
#     "R", "R'", "R2",
#     "L", "L'", "L2",
#     "U", "U'", "U2",
#     "D", "D'", "D2",
#     "F", "F'", "F2",
#     "B", "B'", "B2"
# ]

# # Tworzymy przyciski w kolumnach po 3
# for i in range(0, len(move_names), 3):
#     cols = st.columns(3)
#     for j, move in enumerate(move_names[i:i+3]):
#         if cols[j].button(move):
#             getattr(cube, move)()  # wywołanie odpowiedniego ruchu


col1, col2 = st.columns([2, 1])

cross_length = st.sidebar.number_input("Cross length", value=6)

scramble_input = st.sidebar.text_input("Own scramble")

scramble_length = st.sidebar.number_input("length", value=21)

generate_button = st.sidebar.button("Scramble")

solve_button = st.sidebar.button("Solve")


# with col1:
#     scramble_length = st.sidebar.number_input("length", value=21)

# with col2:
#     generate_button = st.sidebar.button("Scramble")


# st.markdown("### Scramble")
scramble_notation = st.empty()
# st.markdown("---")

# st.markdown("### Cross")
cross_soltion = st.empty()
# st.markdown("---")

# st.markdown("### F2L")
f2l_solution = st.empty()
# st.markdown("---")

# st.markdown("### OLL")
oll_solution = st.empty()
# st.markdown("---")

# st.markdown("### PLL")
pll_solution = st.empty()

if "scramble" not in st.session_state:
    st.session_state.scramble = ""


if generate_button:
    cube.reset()
    if scramble_input:
        st.session_state.scramble = scramble_input
        scramble_notation.text(f"Scramble: {scramble_input}")
        cube.move(scramble_input)
    else:
        scramble = generate_scramble(int(scramble_length))     
        st.session_state.scramble = scramble
        cube.move(scramble)
    scramble_notation.text(f"Scramble: {st.session_state.scramble}")


cross = []
f2l = []
if solve_button:
    cube = Cube(st.session_state.scramble)
    cross = Cross(cube).find_cross(cross_length)
    if cross: 
        cross_soltion.text(f"Cross: {cross[0]}")
        if cross:
            cube.move(cross[0])


        f2l = F2L(cube).solve(verbose=False)
        f2l_solution.text(f"F2L: {f2l}")
        if f2l:
            _ = [cube.move(i) for i in f2l]

        oll = OLL(cube).solve()
        oll_solution.text(f"OLL: {oll}")
        if oll:
            cube.move(oll)

        pll = PLL(cube).solve()
        pll_solution.text(f"PLL: {pll}")
        if pll:
            cube.move(pll)
    else: 
        cross_soltion.text("No solutions")

scramble_notation.text(f"Scramble: {st.session_state.scramble}")


st.sidebar.text(f"Cross: {len(cross)}")

st.sidebar.text(f"F2L: {len(f2l)}")

display.text(st.session_state.scramble)
display.text(f"{str(cube)}")

# U' L F2 D' R2 D B L B R B D2 U' L B' D L' R' B' F' L2