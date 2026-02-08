import streamlit as st
from cube import Cube
from scramble import generate_scramble, remap_scramble_by_color
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from solving_stage import Solving
from tools import inverse
import convert
from copy import deepcopy

# --- inicjalizacja sesji ---
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

cross_color = st.sidebar.selectbox(
    "Wybierz kolor crossa",
    options=['w','r','b','g','o','y'],  # wszystkie możliwe
    index=5  # domyślnie w
)

agree = st.sidebar.checkbox("Wprowadzanie ręczne")
if not agree:
    scramble_input = st.sidebar.text_input(
        "Own scramble", 
        # value="B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"
        value="R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'"
    )
    notation_input = None
else:
    st.sidebar.markdown(
        '<a href="http://localhost:8502"> Prepare scramble </a>', unsafe_allow_html=True
    )
    notation_input = st.sidebar.text_input(
        "Own notation", 
        value="005004153124512222514520025013134133234044450332154135"
    )
    scramble_input = None

def print_debug():
    st.write("cube.corners:",str([st.session_state.cube.corners[i].tolist() for i in parse_numbers(corners_number)]))
    st.write("corners_to_binary:", str(convert.corners_to_binary(st.session_state.cube, parse_numbers(corners_number))))
    st.write("cube.edges:",str([st.session_state.cube.edges[i].tolist() for i in parse_numbers(edges_input)]))
    st.write("edges_to_binary:", str(convert.edges_to_binary(st.session_state.cube, parse_numbers(edges_input))))
    st.write("y_rotate:", st.session_state.cube.y_rotate)
    st.write("solving: ", st.session_state.parent)
        


debug_mode = st.sidebar.checkbox("Debug mode")
if debug_mode:
    with st.sidebar.form("debug_form"):
        corners_number = st.sidebar.text_input("corner number", value="0 1 2 3 4 5 6 7", on_change=print_debug)
        edges_input = st.sidebar.text_input("edges number", value="0 1 2 3 4 5 6 7 8 9 10 11", on_change=print_debug)
    
def parse_numbers(text):
    if not text.strip():
        return []
    try:
        return [int(x) for x in text.split()]
    except ValueError:
        st.error("Wpisz tylko liczby oddzielone spacjami")
        return []

scramble_length = st.sidebar.number_input("length", value=21)
generate_button = st.sidebar.button("Scramble")
reconstruction_button = st.sidebar.button("Reconstruction")

scramble_notation = st.empty()
if "scramble" not in st.session_state:
    st.session_state.scramble = ""

# --- generowanie scramble ---
if generate_button:
    st.session_state.cube.reset()
    if not agree:
        if scramble_input:
            st.session_state.scramble = scramble_input
        else:
            st.session_state.scramble = generate_scramble(int(scramble_length))
        scramble_notation.text(f"Scramble: {st.session_state.scramble}")
        st.session_state.cube = Cube(notation=st.session_state.scramble)
    else:
        st.session_state.scramble = notation_input
        st.session_state.cube = Cube(state=notation_input)
        
    scramble_notation.text(f"Scramble: {st.session_state.scramble}")

# --- rekonstrukcja całej sekwencji ---
if reconstruction_button:
    if not agree:
        cube = Cube(color=cross_color, notation=st.session_state.scramble)
    else:
        cube = Cube(color=cross_color, state=st.session_state.scramble)
    st.session_state.cube = cube
    solving = Solving(cube)
    st.session_state.solving = solving.build_tree(cross_length)
    st.session_state.total_cross = solving.total_cross
    st.session_state.total_f2l = solving.total_f2l
    st.session_state.total_oll = solving.total_oll
    st.session_state.total_pll = solving.total_pll

# --- przyciski do poruszania się po drzewie rozwiązań ---
def go_forward(item):
    st.session_state.parent = item
    st.session_state.solving = item.child
    st.session_state.cube = item.cube
    if debug_mode:
        print_debug()

        
def go_back():
    prev = st.session_state.parent.parent
    if prev:
        st.session_state.parent = prev
        st.session_state.solving = prev.child
        st.session_state.cube = prev.cube
    if debug_mode:
        print_debug()






if st.session_state.solving:
    for item in st.session_state.solving:
        col1, col2 = st.columns([1,7])
        with col1:
            st.write(item.name)
        with col2:
            st.button(item.alg, on_click=go_forward, args=(item,))
    if st.session_state.parent:
        st.button(f"Back ({inverse(st.session_state.parent.alg)})", on_click=go_back)

# --- podsumowanie i wyświetlenie stanu ---
scramble_notation.text(f"Scramble: {st.session_state.scramble}")
st.sidebar.text(f"Cross: {st.session_state.total_cross}")
st.sidebar.text(f"F2L:   {st.session_state.total_f2l}")
st.sidebar.text(f"OLL:   {st.session_state.total_oll}")
st.sidebar.text(f"PLL:   {st.session_state.total_pll}")




display.text(st.session_state.scramble)
display.text(f"{str(st.session_state.cube)}")
