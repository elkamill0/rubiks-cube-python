import streamlit as st
from cube import Cube
from scramble import generate_scramble
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from solving_stage import Solving


# Inicjalizacja kostki w sesji
if "cube" not in st.session_state:
    st.session_state.cube = Cube()

if "solving" not in st.session_state:
    st.session_state.solving = False
    st.session_state.total_cross = 0
    st.session_state.total_f2l = 0
    st.session_state.total_oll = 0
    st.session_state.total_pll = 0

cube = st.session_state.cube

display = st.empty()  # miejsce do wyświetlania kostki




col1, col2 = st.columns([2, 1])

cross_length = st.sidebar.number_input("Cross length", value=6)

scramble_input = st.sidebar.text_input("Own scramble", value="B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2")

scramble_length = st.sidebar.number_input("length", value=21)

generate_button = st.sidebar.button("Scramble")

reconstruction_button = st.sidebar.button("Reconstruction")


# st.markdown("### Scramble")
scramble_notation = st.empty()
# st.markdown("---")

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



if reconstruction_button:
    cube = Cube(st.session_state.scramble)
    solving = Solving(cube)
    st.session_state.solving = solving.build_tree(cross_length)
    st.session_state.total_cross = solving.total_cross
    st.session_state.total_f2l = solving.total_f2l
    st.session_state.total_oll = solving.total_oll
    st.session_state.total_pll = solving.total_pll

if st.session_state.solving:
    for item in st.session_state.solving:
        col1, col2 = st.columns([1,7])
        with col1:
            st.write(item.name)
        with col2:
            if st.button(item.alg):
                st.session_state.parent = item.parent
                st.session_state.solving = item.child
                st.session_state.cube = item.cube
                st.rerun()


scramble_notation.text(f"Scramble: {st.session_state.scramble}")

st.sidebar.text(f"Cross: {st.session_state.total_cross}")
st.sidebar.text(f"F2L:   {st.session_state.total_f2l}")
st.sidebar.text(f"OLL:   {st.session_state.total_oll}")
st.sidebar.text(f"PLL:   {st.session_state.total_pll}")

display.text(st.session_state.scramble)
display.text(f"{str(st.session_state.cube)}")
