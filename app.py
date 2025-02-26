import streamlit as st
import random

# Sample words and their positions for crossword
words = {
    "apple": [(0, 0, "right")],
    "banana": [(2, 1, "down")],
    "cherry": [(4, 2, "right")],
    "date": [(1, 4, "down")],
    "grape": [(3, 3, "right")]
}

grid_size = 10
crossword_grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Place words in the grid
def place_words():
    for word, positions in words.items():
        for x, y, direction in positions:
            if direction == "right":
                for i, letter in enumerate(word):
                    crossword_grid[y][x + i] = letter
            elif direction == "down":
                for i, letter in enumerate(word):
                    crossword_grid[y + i][x] = letter

place_words()

# Initialize session state for tracking progress
if 'guesses' not in st.session_state:
    st.session_state.guesses = {}

st.title("Crossword Puzzle")

# Display crossword grid with masked letters
for y in range(grid_size):
    row_display = " "
    for x in range(grid_size):
        char = crossword_grid[y][x]
        if char == ' ' or (x, y) in st.session_state.guesses:
            row_display += f"{char} "
        else:
            row_display += "_ "
    st.write(row_display)

# User input
user_word = st.text_input("Enter a word:").strip().lower()

# Check the guess
if user_word:
    if user_word in words:
        st.success(f"🎉 Correct! '{user_word}' is in the crossword!")
        for x, y, direction in words[user_word]:
            if direction == "right":
                for i, letter in enumerate(user_word):
                    st.session_state.guesses[(x + i, y)] = letter
            elif direction == "down":
                for i, letter in enumerate(user_word):
                    st.session_state.guesses[(x, y + i)] = letter
    else:
        st.error("❌ Incorrect! Try another word.")

# Button to restart the game
if st.button("Restart Puzzle"):
    st.session_state.guesses = {}
    st.experimental_rerun()


