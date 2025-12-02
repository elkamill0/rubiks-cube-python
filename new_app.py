import streamlit as st
from cube import Cube
from scramble import generate_scramble
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from solving_stage import Solving
from tools import inverse
import convert


if "cube" not in st.session_state:
    st.session_state.cube = Cube()

if "solving" not in st.session_state:
    st.session_state.solving = False
    st.session_state.total_cross = 0
    st.session_state.total_f2l = 0
    st.session_state.total_oll = 0
    st.session_state.total_pll = 0
    st.session_state.parent = None
    st.session_state.name = None

cube = st.session_state.cube

display = st.empty()


col1, col2 = st.columns([2, 1])

cross_length = st.sidebar.number_input("Cross length", value=6)

agree = st.sidebar.checkbox("Wprowadzanie ręczne")

if not agree:
    scramble_input = st.sidebar.text_input("Own scramble", value="B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2")
    notation_input = None
else:
    st.sidebar.markdown(
        '<a href="http://localhost:8502"> Prepare scramble </a>', unsafe_allow_html=True,
    )
    notation_input = st.sidebar.text_input("Own notation", value="005004153124512222514520025013134133234044450332154135")
    scramble_input = None

scramble_length = st.sidebar.number_input("length", value=21)

generate_button = st.sidebar.button("Scramble")

reconstruction_button = st.sidebar.button("Reconstruction")


scramble_notation = st.empty()

if "scramble" not in st.session_state:
    st.session_state.scramble = ""


if generate_button:
    cube.reset()
    if not agree:
        if scramble_input:
            st.session_state.scramble = scramble_input
            scramble_notation.text(f"Scramble: {scramble_input}")
            cube.move(scramble_input)
        else:
            scramble = generate_scramble(int(scramble_length))     
            st.session_state.scramble = scramble
            cube.move(scramble)
    
    else:
        st.session_state.scramble = notation_input
        cube.corners, cube.edges, cube.centers = convert.state_to_cube(state=notation_input)
        # cube = Cube(state=notation_input)
        scramble_notation.text(f"Scramble: {notation_input}")
        
    scramble_notation.text(f"Scramble: {st.session_state.scramble}")



if reconstruction_button:
    if not agree:
        cube = Cube(notation=st.session_state.scramble)
    else:
        cube = Cube(state=st.session_state.scramble)
        
    solving = Solving(cube)
    st.session_state.solving = solving.build_tree(cross_length)
    st.session_state.total_cross = solving.total_cross
    st.session_state.total_f2l = solving.total_f2l
    st.session_state.total_oll = solving.total_oll
    st.session_state.total_pll = solving.total_pll


def go_forward(item):
    st.session_state.parent = item
    st.session_state.solving = item.child
    st.session_state.cube = item.cube

def go_back():
    prev = st.session_state.parent.parent
    if prev:
        st.session_state.parent = prev
        st.session_state.solving = prev.child
        st.session_state.cube = prev.cube


if st.session_state.solving:
    for item in st.session_state.solving:
        col1, col2 = st.columns([1,7])
        with col1:
            st.write(item.name)
        with col2:
            st.button(item.alg, on_click=go_forward, args=(item,))
    if st.session_state.parent:
        st.button(f"Back ({inverse(st.session_state.parent.alg)})", on_click=go_back) 

scramble_notation.text(f"Scramble: {st.session_state.scramble}")

st.sidebar.text(f"Cross: {st.session_state.total_cross}")
st.sidebar.text(f"F2L:   {st.session_state.total_f2l}")
st.sidebar.text(f"OLL:   {st.session_state.total_oll}")
st.sidebar.text(f"PLL:   {st.session_state.total_pll}")

display.text(st.session_state.scramble)
display.text(f"{str(st.session_state.cube)}")
