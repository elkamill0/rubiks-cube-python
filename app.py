import streamlit as st
import random
from cube import Cube
import scramble

# ---------- CONFIG ---------- #
st.set_page_config(layout="wide")
colors = ["white", "yellow", "red", "orange", "green", "blue"]
color_emojis = {
    "white": "⬜", "yellow": "🟨", "red": "🟥",
    "orange": "🟧", "green": "🟩", "blue": "🟦",
}
default_colors = {
    "U": "white", "D": "yellow", "F": "green",
    "B": "blue", "L": "orange", "R": "red"
}
color_numbers = {
    "white": "0", "orange": "1", "green": "2",
    "red": "3", "blue": "4", "yellow": "5"
}

# ---------- STATE INIT ---------- #
if "cube" not in st.session_state:
    st.session_state.cube = {
        face: [[default_colors[face]] * 3 for _ in range(3)]
        for face in ["U", "L", "F", "R", "B", "D"]
    }

# ---------- GUI ---------- #
def styled_emoji(color):
    return f"<div style='text-align:center; font-size:28px; width:40px; height:40px;'>{color_emojis[color]}</div>"

def render_face(face_key):
    st.markdown(f"#### {face_key}")
    face = st.session_state.cube[face_key]
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            key = f"{face_key}-{row}-{col}"
            current_color = face[row][col]
            if key not in st.session_state:
                st.session_state[key] = current_color
            with cols[col]:
                selected = st.selectbox(
                    " ", colors,
                    index=colors.index(st.session_state[key]),
                    format_func=lambda c: color_emojis[c],
                    label_visibility="collapsed",
                    key=key
                )
            face[row][col] = selected

def losuj_realistycznie():
    all_colors = sum([[color] * 9 for color in colors], [])
    random.shuffle(all_colors)
    idx = 0
    for face in ["U", "L", "F", "R", "B", "D"]:
        for row in range(3):
            for col in range(3):
                kolor = all_colors[idx]
                st.session_state.cube[face][row][col] = kolor
                st.session_state[f"{face}-{row}-{col}"] = kolor
                idx += 1

def cube_gui_to_state_string():
    state_str = ""
    for face in ["U", "L", "F", "R", "B", "D"]:
        for row in st.session_state.cube[face]:
            for color in row:
                state_str += color_numbers[color]
    return state_str

# ---------- INTERFACE ---------- #
st.title("🧊 Rubik's Cube App")

with st.sidebar:
    if st.button("🔀 Wylosuj realistyczne kolory"):
        losuj_realistycznie()

    if st.button("🔁 Reset"):
        for face in ["U", "L", "F", "R", "B", "D"]:
            for row in range(3):
                for col in range(3):
                    color = default_colors[face]
                    st.session_state.cube[face][row][col] = color
                    st.session_state[f"{face}-{row}-{col}"] = color

    if st.button("🎲 Scramble"):
        moves = scramble.generate_scramble(20)
        st.session_state.scramble_moves = moves
        cube = Cube()
        cube.move(moves)
        new_state = cube.get_state()
        face_order = ["U", "L", "F", "R", "B", "D"]
        for i, face in enumerate(face_order):
            for row in range(3):
                for col in range(3):
                    idx = i * 9 + row * 3 + col
                    val = new_state[idx]
                    color = list(color_numbers.keys())[list(color_numbers.values()).index(val)]
                    st.session_state.cube[face][row][col] = color
                    st.session_state[f"{face}-{row}-{col}"] = color

    st.markdown("### ➡️ Wykonaj ruch")
    move_input = st.text_input("Wprowadź notację (np. R U R')", key="move_input")
    if st.button("▶️ Wykonaj ruch"):
        move_seq = st.session_state.move_input
        state_str = cube_gui_to_state_string()
        cube = Cube(state=state_str)
        cube.move(move_seq)
        new_state = cube.get_state()
        face_order = ["U", "L", "F", "R", "B", "D"]
        for i, face in enumerate(face_order):
            for row in range(3):
                for col in range(3):
                    idx = i * 9 + row * 3 + col
                    val = new_state[idx]
                    color = list(color_numbers.keys())[list(color_numbers.values()).index(val)]
                    st.session_state.cube[face][row][col] = color
                    st.session_state[f"{face}-{row}-{col}"] = color

    if st.button("📋 Pokaż stan jako string"):
        st.code(cube_gui_to_state_string(), language="text")

# ---------- MAIN DISPLAY ---------- #
st.markdown("## 🔧 Edytuj ścianki")
st.markdown("### Góra (U)")
render_face("U")

st.markdown("### Lewa (L), Przód (F), Prawa (R), Tył (B)")
cols = st.columns(4)
for i, face in enumerate(["L", "F", "R", "B"]):
    with cols[i]:
        render_face(face)

st.markdown("### Dół (D)")
render_face("D")
