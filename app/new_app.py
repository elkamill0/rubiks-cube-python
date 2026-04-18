import streamlit as st
from cube import Cube
from scramble import generate_scramble, remap_scramble_by_color
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from solving_stage import Solving, Manual
from tools import inverse
import convert
from copy import deepcopy

if "cube" not in st.session_state:
    st.session_state.cube = Cube()

if "solving" not in st.session_state:
    st.session_state.solving = False
    st.session_state.total_cross = 0
    st.session_state.total_f2l = 0
    st.session_state.total_oll = 0
    st.session_state.total_pll = 0
    st.session_state.parent = None
    st.session_state.manual = []

cube = st.session_state.cube
display = st.empty()
col1, col2 = st.columns([2, 1])

auto_cross_length = st.sidebar.checkbox("Auto cross length")
cross_length = st.sidebar.number_input(
    "Cross length", min_value=0, step=1, value=6, disabled=auto_cross_length
)


cross_color = st.sidebar.selectbox(
    "Cross color", options=["w", "r", "b", "g", "o", "y"], index=5
)

agree = st.sidebar.checkbox("Manual state")
if not agree:
    scramble_input = st.sidebar.text_input(
        "Own scramble", value="R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'"
    )
    notation_input = None
else:
    st.sidebar.markdown(
        '<a href="http://localhost:8502"> Prepare scramble </a>', unsafe_allow_html=True
    )
    notation_input = st.sidebar.text_input(
        "Own notation", value="005004153124512222514520025013134133234044450332154135"
    )
    scramble_input = None


def print_debug():
    st.write(
        "cube.corners:",
        str(
            [
                st.session_state.cube.corners[i].tolist()
                for i in parse_numbers(corners_number)
            ]
        ),
    )
    st.write(
        "corners_to_binary:",
        str(
            convert.corners_to_binary(
                st.session_state.cube, parse_numbers(corners_number)
            )
        ),
    )
    st.write(
        "cube.edges:",
        str(
            [
                st.session_state.cube.edges[i].tolist()
                for i in parse_numbers(edges_input)
            ]
        ),
    )
    st.write(
        "edges_to_binary:",
        str(convert.edges_to_binary(st.session_state.cube, parse_numbers(edges_input))),
    )
    st.write("y_rotate:", st.session_state.cube.y_rotate)
    st.write("solving: ", st.session_state.parent)


debug_mode = st.sidebar.checkbox("Debug mode")
if debug_mode:
    with st.sidebar.form("debug_form"):
        corners_number = st.sidebar.text_input(
            "corner number", value="0 1 2 3 4 5 6 7", on_change=print_debug
        )
        edges_input = st.sidebar.text_input(
            "edges number", value="0 1 2 3 4 5 6 7 8 9 10 11", on_change=print_debug
        )
        st.sidebar.text_input(
            "Enter moves",
            key="moves_text",
            on_change=lambda: st.session_state.cube.move(st.session_state.moves_text),
        )


def parse_numbers(text):
    if not text.strip():
        return []
    try:
        return [int(x) for x in text.split()]
    except ValueError:
        st.error("Wpisz tylko liczby oddzielone spacjami")
        return []


scramble_length = st.sidebar.number_input("length", value=21)
scramble_button = st.sidebar.button("Scramble")
reconstruction_button = st.sidebar.button("Reconstruction")
reconstruction_step_by_step_button = st.sidebar.button("Reconstruction (step by step)")

scramble_notation = st.empty()
if "scramble" not in st.session_state:
    st.session_state.scramble = ""

if scramble_button:
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

if reconstruction_button:
    st.session_state.manual = None

    if not agree:
        cube = Cube(color=cross_color, notation=st.session_state.scramble)
    else:
        cube = Cube(color=cross_color, state=st.session_state.scramble)
    st.session_state.cube = cube
    solving = Solving(cube)

    def find_solution():
        if auto_cross_length:
            for length in range(8):
                st.write(f"Trying length: {length}")
                result = solving.build_tree(length)
                if result:
                    return result
            return None
        else:
            st.write(f"Cross length: {cross_length}")
            return solving.build_tree(cross_length)

    st.session_state.build_tree = find_solution()
    st.session_state.solving = solving
    st.session_state.total_cross = solving.total_cross
    st.session_state.total_f2l = solving.total_f2l
    st.session_state.total_oll = solving.total_oll
    st.session_state.total_pll = solving.total_pll

if reconstruction_step_by_step_button or st.session_state.manual:
    st.session_state.solving = False
    st.session_state.manual = Manual(
        st.session_state.cube, cross_length=cross_length
    ).loop()
    for i, (alg, name) in enumerate(st.session_state.manual):
        cols = st.columns([1, 3])

        cols[0].write(name)

        if cols[1].button(alg, key=f"btn_{i}"):
            st.session_state.cube.apply_step((alg, name))
            st.rerun()

    if st.session_state.cube.log:
        if st.button(f"Back: {inverse(st.session_state.cube.log[-1])}", key="Back"):
            st.session_state.cube.undo()
            st.rerun()


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
    st.title("Solutions")
    for i, (log_names, moves) in enumerate(st.session_state.solving.shortest_path, 1):
        st.subheader(f"Solution {i}")
        st.write("Moves:")
        st.code("\n".join(log_names), language="text")
        st.write(f"Total moves: {moves}")
        st.divider()


scramble_notation.text(f"Scramble: {st.session_state.scramble}")
st.sidebar.text(f"Cross: {st.session_state.total_cross}")
st.sidebar.text(f"F2L:   {st.session_state.total_f2l}")
st.sidebar.text(f"OLL:   {st.session_state.total_oll}")
st.sidebar.text(f"PLL:   {st.session_state.total_pll}")


display.text(st.session_state.scramble)
display.text(f"{str(st.session_state.cube)}")
